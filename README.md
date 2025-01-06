# Measuring-Air-Quality-Index
---

# **Air Quality Index (AQI) Prediction Web Application**

This project is a web-based application that predicts the **Air Quality Index (AQI)** category based on user-input pollutant levels. The app provides an intuitive and visually appealing interface, allowing users to input pollutant concentrations such as **PM2.5**, **PM10**, **NO₂**, **SO₂**, **CO**, and **O₃**. The model then predicts the air quality category (e.g., **Good**, **Moderate**, **Poor**, etc.) and displays the result dynamically.

---

## **Features**

1. **Interactive User Interface:**
   - A modern, sleek design with a background illustrating air quality differences between clean and polluted air.
   - Easy-to-use form for inputting pollutant levels.

2. **Real-Time Prediction:**
   - Dynamically displays the predicted air quality category after input submission without reloading the page.

3. **Categories of Prediction:**
   - Good
   - Satisfactory
   - Moderate
   - Poor
   - Very Poor
   - Severe

4. **Responsive Design:**
   - The app is fully responsive and works on both desktop and mobile devices.

---

## **Technologies Used**

1. **Frontend:**
   - HTML
   - CSS
   - JavaScript

2. **Backend:**
   - Flask (Python Web Framework)

3. **Machine Learning:**
   - TensorFlow (Neural Network Model)
   - Scikit-learn (Data Preprocessing)

4. **Styling:**
   - Custom CSS for form design, buttons, and responsiveness.
   - A custom background image to enhance the user experience.

---

## **How to Run the Project**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-username/air-quality-index-prediction.git
cd air-quality-index-prediction
```

### **Step 2: Set Up Virtual Environment**
```bash
python -m venv venv
```

Activate the virtual environment:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### **Step 3: Install Dependencies**
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### **Step 4: Run the Flask Application**
```bash
python app.py
```

The app will run on **`http://127.0.0.1:5000`**. Open this URL in your browser to access the application.

---

## **Dataset and Model**

- **Dataset:** Air quality data from Indian cities (2015-2020), sourced from [Kaggle](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india).
- **Model:** A neural network trained on pollutant data to classify air quality into six categories.

---

## **Screenshots**

### **Before Prediction**
This is how the application looks before entering pollutant values:

![Screenshot 2025-01-06 200539](https://github.com/user-attachments/assets/4665b6e1-2021-404e-9cd3-c0cc5ae94436)

---

### **After Prediction**
This is how the application displays the predicted air quality after entering the pollutant values:

![Screenshot 2025-01-06 200631](https://github.com/user-attachments/assets/b7fd4809-d6aa-444d-af7e-294c3cc305f2)

---

## **File Structure**

```
air-quality-index/
│
├── app.py                   # Main Flask application
├── model/
│   └── best_combined_air_quality_model.h5  # Trained neural network model
├── static/
│   ├── background.webp      # Background image
│   ├── style.css            # Custom CSS styles
│   └── screenshots/         # Folder for screenshots
│       ├── before_prediction.png
│       └── after_prediction.png
├── templates/
│   └── index.html           # HTML file for the web interface
├── venv/                    # Virtual environment folder
├── requirements.txt         # List of required Python packages
└── README.md                # Project documentation
```

---

## **Future Enhancements**

1. Improve the model by using more advanced machine learning algorithms or pre-trained models like TabNet.
2. Add additional features, such as:
   - Historical air quality trends.
   - Suggestions to improve air quality based on predictions.
3. Deploy the app to cloud platforms like Heroku or AWS for public use.

---

## **Acknowledgments**

- **Kaggle** for providing the air quality dataset.
- **TensorFlow** and **Flask** communities for their comprehensive documentation and support.
- under guidance of [Dr Agughasi Victor Ikechukwu](https://github.com/Victor-Ikechukwu)

---
