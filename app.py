from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('model/best_combined_air_quality_model.h5')

# Load the scaler (you can replace this with your actual scaler if saved)
scaler = StandardScaler()
sample_data = pd.DataFrame([[50, 40, 20, 10, 0.5, 0.1]], columns=['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3'])
scaler.fit(sample_data)

# AQI categories as used in training
aqi_categories = ['Good', 'Satisfactory', 'Moderate', 'Poor', 'Very Poor', 'Severe']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Extract data from the form
            pm25 = float(request.form['pm25'])
            pm10 = float(request.form['pm10'])
            no2 = float(request.form['no2'])
            so2 = float(request.form['so2'])
            co = float(request.form['co'])
            o3 = float(request.form['o3'])

            # Prepare the input for the model
            input_data = np.array([[pm25, pm10, no2, so2, co, o3]])
            input_data_scaled = scaler.transform(input_data)

            # Predict the AQI category
            prediction = model.predict(input_data_scaled)
            predicted_class = np.argmax(prediction, axis=1)[0]
            predicted_aqi = aqi_categories[predicted_class]

            # Return the result as a response
            return jsonify({'prediction': f'The predicted air quality is: {predicted_aqi}'})

        except Exception as e:
            return jsonify({'error': f'Error occurred: {str(e)}'})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
