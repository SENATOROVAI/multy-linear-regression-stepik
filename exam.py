import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    'area': [30, 50, 60, 80, 100],
    'rooms': [1, 2, 2, 3, 4],
    'price': [3.5, 5.5, 6.5, 8.5, 10.0]
})

X = data[['area', 'rooms']]
y = data['price']

# Обучение модели
model = LinearRegression()
model.fit(X, y)

# Коэффициенты
b0 = model.intercept_
b1, b2 = 

print(f"Уравнение: price = {b0:.2f} + {b1:.2f}*area + {b2:.2f}*rooms")

X_np = np.column_stack((np.ones(len(X)), X))
y_np = y.to_numpy()

det = np.linalg.det()
rank = np.linalg.matrix_rank()

