# Housing Data ETL & Machine Learning Pipeline

## Overview
This project consists of two main components:
1. **ETL (Extract, Transform, Load) Pipeline**: Processes housing market data by extracting from a CSV file, transforming key attributes, and loading the cleaned data into a MySQL database.
2. **Machine Learning Model**: Implements a linear regression model to predict housing prices based on key features from the dataset.

---

## **1️⃣ ETL Pipeline**

### Features
- **Extract**: Reads housing data from a CSV file.
- **Transform**:
  - Converts `median_house_value` to thousands.
  - Calculates `bedrooms_per_room` ratio.
  - Removes duplicate rows.
- **Load**: Saves the transformed data into a MySQL table.

### Technologies Used
- **Python** (pandas, SQLAlchemy)
- **MySQL** (for storing processed data)

### Installation
#### Prerequisites
Ensure you have Python and the required dependencies installed:
```bash
pip install pandas sqlalchemy pymysql
```

#### Database Setup
Create a MySQL database (`myDB`) and configure user permissions accordingly. Update the `db_url` in `main()` to match your database credentials.

### Usage
1. Place your CSV file in the specified directory (`/Users/szabokornel/Downloads/housing.csv`).
2. Run the script:
   ```bash
   python script.py
   ```
3. The cleaned data will be loaded into the `housing` table in MySQL.

### Configuration
Modify these variables in `main()` to match your setup:
```python
file_path = '/path/to/housing.csv'
db_url = "mysql+pymysql://username:password@localhost:3306/database_name"
```

### Notes
- Ensure MySQL is running and accessible before executing the script.
- Update database credentials for security before deploying.

---

## **2️⃣ Machine Learning Model**

### Features
- **Data Preprocessing**:
  - Scales `median_income` and `median_house_value`.
  - Fills missing values in `total_bedrooms` and `bedrooms_per_room`.
  - Encodes categorical features (`ocean_proximity`).
- **Model Training**:
  - Uses **Linear Regression** to predict `median_house_value`.
  - Trains the model on selected features.
- **Prediction**:
  - Allows new data input to predict housing prices.
  - Evaluates the model using R² (coefficient of determination).

### Dependencies
Ensure you have the required libraries installed:
```bash
pip install pandas scikit-learn
```

### Usage
1. Prepare the dataset: `housing_v2.csv`.
2. Run the script:
   ```bash
   python ml_model.py
   ```
3. The script will output the predicted house price and R² score.

### Code Overview
#### **Data Preparation**
```python
import pandas as pd

df = pd.read_csv(r'/Users/szabokornel/Downloads/housing_v2.csv')
df['median_income'] = df['median_income'] * 10000
df['median_house_value'] = df['median_house_value'] * 1000

# Fill missing values
df["total_bedrooms"].fillna(df["total_bedrooms"].median(), inplace=True)
df["bedrooms_per_room"].fillna(df["bedrooms_per_room"].median(), inplace=True)

# Encode categorical variables
df = pd.get_dummies(df, columns=["ocean_proximity"], prefix="ocean")
```

#### **Model Training & Prediction**
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

features = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'bedrooms_per_room', 'ocean_<1H OCEAN', 'ocean_INLAND', 'ocean_NEAR BAY']
target = 'median_house_value'
X = df[features]
y = df[target]

model = LinearRegression()
model.fit(X, y)

# Predict on new data
new_data = pd.DataFrame({
    'longitude': [-123.24],
    'latitude': [39.85],
    'housing_median_age': [64],
    'total_rooms': [1500],
    'total_bedrooms': [200],
    'population': [500],
    'households': [200],
    'median_income': [50000],
    'bedrooms_per_room': [0.13],
    'ocean_<1H OCEAN': [0],
    'ocean_INLAND': [0],
    'ocean_NEAR BAY': [0]
})

predicted_value = model.predict(new_data)
print(f"Predicted House Value: {predicted_value[0]}")

# Model Evaluation
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)
print(f"R² Score: {r2}")
```

---

## License
This project is open-source and available for modification as needed.

