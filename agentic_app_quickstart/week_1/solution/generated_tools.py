from helpers import read_employee_data, read_sample_sale_data, read_weather_data
from agents import function_tool

@function_tool
def predict_salary_xgboost(department: str, hire_date: str, performance_score: float) -> float:
    """
    Trains a simple XGBoost regression model to predict salary based on department, hire date, and performance score,
    and then predicts the salary for an individual with the provided features.
    
    Training features:
        - department (categorical string)
        - hire_date (string in YYYY-MM-DD format)
        - performance_score (float)
    Target:
        - salary (float)

    Prediction input:
        - department: str, e.g., 'Marketing'
        - hire_date: str, e.g., '2022-05-08' (format must match training data)
        - performance_score: float, e.g., 3.0
    
    Returns:
        - predicted_salary: float
    """
    import pandas as pd
    import xgboost as xgb
    from sklearn.preprocessing import LabelEncoder
    from sklearn.model_selection import train_test_split

    # Read employee data
    df = read_employee_data().copy()
    
    # Preprocess features
    label_encoder = LabelEncoder()
    df['department_enc'] = label_encoder.fit_transform(df['department'])
    # Convert hire_date to ordinal (days since 1970-01-01)
    df['hire_date_ordinal'] = pd.to_datetime(df['hire_date']).map(pd.Timestamp.toordinal)

    # Feature matrix and target
    X = df[['department_enc', 'hire_date_ordinal', 'performance_score']]
    y = df['salary']

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train XGBoost model
    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Prepare new sample
    department_enc = label_encoder.transform([department])[0]
    hire_date_ordinal = pd.to_datetime(hire_date).toordinal()
    perf_score = performance_score
    X_new = pd.DataFrame([[department_enc, hire_date_ordinal, perf_score]], columns=['department_enc', 'hire_date_ordinal', 'performance_score'])

    # Predict
    predicted_salary = float(model.predict(X_new)[0])
    return predicted_salary
