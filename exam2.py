import numpy as np
import pandas as pd

data = pd.DataFrame({
    'x1': [1, 2, 3, 4, 5],
    'x2': [2, 4, 6, 8, 10],  
    'y':  [3, 6, 9, 12, 15]  
})

X = data[['x1', 'x2']]
X_np = np.column_stack((np.ones(len(X)), X))
y = data['y'].to_numpy()

det = np.linalg.det()
rank = np.linalg.matrix_rank()

