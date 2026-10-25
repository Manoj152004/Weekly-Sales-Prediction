# 📊 Weekly Sales Prediction

A Machine Learning project that predicts weekly retail sales based on store information, date features, holiday status, and economic indicators.

## 🎯 Project Objective

The goal of this project is to predict weekly sales using historical retail data and a trained Machine Learning model. The project includes a Streamlit web application that lets users enter relevant information and receive a sales prediction.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Git and GitHub

## 📂 Project Structure

```text
Sales_Prediction/
├── app.py
├── sales_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## 🔄 Machine Learning Workflow

1. **Data collection** — use a historical weekly retail sales dataset.
2. **Data preparation** — load the dataset and inspect its columns and data types.
3. **Data cleaning** — check for missing values, invalid values, and data quality issues.
4. **Feature engineering** — extract Year, Month, Day, and Week from the Date column.
5. **Feature selection** — use Store, Year, Month, Day, Week, Holiday_Flag, Temperature, Fuel_Price, CPI, and Unemployment as model inputs.
6. **Train and validate** — split the data into training and validation sets.
7. **Model training** — train a HistGradientBoostingRegressor inside a Scikit-learn preprocessing pipeline.
8. **Model evaluation** — evaluate predictions using suitable regression metrics such as R², MAE, and RMSE.
9. **Model saving** — save the trained pipeline as `sales_model.pkl`.
10. **Deployment interface** — build a Streamlit app that accepts inputs and displays predicted weekly sales.
11. **Version control** — manage and publish project files with Git and GitHub.

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Manoj152004/Weekly-Sales-Prediction.git
cd Weekly-Sales-Prediction
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the Streamlit application

```bash
python -m streamlit run app.py
```

The application should open in your browser. If it does not, open the local URL shown in the terminal, usually `http://localhost:8501`.

## 🧾 Model Inputs

The application uses the following features:

| Feature | Description |
|---|---|
| Store | Store identifier |
| Year | Year of the sales week |
| Month | Month |
| Day | Day of month |
| Week | Week number |
| Holiday_Flag | Whether the week is a holiday week (0 or 1) |
| Temperature | Temperature value |
| Fuel_Price | Fuel price |
| CPI | Consumer Price Index |
| Unemployment | Unemployment rate |

Enter values in the units and ranges used by the training dataset for meaningful predictions.

## 📈 Model Evaluation

The model was trained using a Scikit-learn pipeline and saved for use by the Streamlit application. Model performance should be reported using results measured on a held-out test set. Performance on a random split may differ from performance on future dates.

## ⚠️ Limitations

- Predictions depend on the quality and representativeness of the training data.
- User-entered values outside the training data range may produce unreliable predictions.
- The saved model must be loaded with compatible Python and library versions.
- The application currently provides predictions from a saved model; it does not retrain the model through the website.

## 🔮 Future Improvements

- Deploy the app publicly using a hosting service such as Streamlit Community Cloud.
- Add visualizations for historical sales.
- Improve input validation and user experience.
- Compare additional regression models.
- Add model evaluation charts and documented test-set metrics.

## 👨‍💻 Author

**Manoj Kumar**

Aspiring Data Scientist | Python | SQL | Excel

GitHub: [@Manoj152004](https://github.com/Manoj152004)

---

*This project was created as a hands-on learning project to practice Machine Learning, Python, and web app development.*