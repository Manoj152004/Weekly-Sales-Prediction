
# Weekly Sales Prediction

## About the Project
This project uses Machine Learning to predict weekly sales based on store information, dates, holidays, temperature, fuel prices, CPI, and unemployment.

The trained model is integrated into a Streamlit web application so users can enter values and get sales predictions.

## Features
- Weekly sales prediction
- Interactive Streamlit web application
- Trained Machine Learning model saved using Joblib
- Simple and user-friendly interface

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## Project Structure
```text
Weekly-Sales-Prediction/
├── app.py
├── sales_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## Input Features
The model uses these features:
1. Store
2. Year
3. Month
4. Day
5. Week
6. Holiday_Flag
7. Temperature
8. Fuel_Price
9. CPI
10. Unemployment

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Manoj152004/Weekly-Sales-Prediction.git
cd Weekly-Sales-Prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```

The application will open in your web browser.

## How It Works
1. The user enters the required store and environmental information.
2. The application sends the input features to the trained model.
3. The model predicts weekly sales.
4. The prediction is displayed in the Streamlit application.

## Project Goal
The goal of this project is to practice Machine Learning and deploy a trained model through an interactive web application.

## Author
Manoj

## Disclaimer
This project is intended for educational and learning purposes. Prediction quality depends on the training data and model performance.
