## Linear Regression

```py
from sklearn.linear_model import LinearRegression

model = LinearRegression()
LR = model.fit(x, y)

x_range = np.linspace(X.min(), X.max(), 20)
y_range = model.predict(x_range.reshape(-1, 1))
```

## Lowess Regression (Kernel Smoothing)

Stands for Locally Weighted Scatterplot Smoothing. A non-parametric fitting technique that doesn't require data to follow any specific distribution, but that means you won't have a global equation to predict values of new data points.

### statsmodels

```py
import numpy as np
import statsmodels.api as sm

lowess = sm.nonparametric.lowess
x = np.random.uniform(low = -2*np.pi, high = 2*np.pi, size=500)
y = np.sin(x) + np.random.normal(size=len(x))
z = lowess(y, x)
w = lowess(y, x, frac=1./3)
```

### Seaborn

Has built Lowess modelling.
