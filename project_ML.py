#project_ML

#adatelokeszites

import pandas as pd

df = pd.read_csv(r'/Users/szabokornel/Downloads/housing_v2.csv')
df['median_income'] = df['median_income'] * 10000
df['median_house_value'] = df['median_house_value'] * 1000

#szarmaztatott adatok letrehozasa

df["total_bedrooms"].fillna(df["total_bedrooms"].median(), inplace=True)
df["bedrooms_per_room"].fillna(df["bedrooms_per_room"].median(), inplace=True)

df = pd.get_dummies(df, columns=["ocean_proximity"], prefix="ocean")

#ML modell

features = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'bedrooms_per_room', 'ocean_<1H OCEAN', 'ocean_INLAND', 'ocean_NEAR BAY']
target = 'median_house_value'
X = df[features]
y = df[target]

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X,y)

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
print(f"Az előrejelzett érték: {predicted_value[0]}")

from sklearn.metrics import r2_score

y_pred = model.predict(X)
r2 = r2_score(y, y_pred)
print(f"R-négyzet érték: {r2}")