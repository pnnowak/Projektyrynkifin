from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from ladowaniedata import ladowanie_data

sp500 = ladowanie_data()
X_train, X_test, y_train, y_test = train_test_split(sp500['Open'], sp500['Close'], test_size=0.2, random_state=123)
y_mean = np.mean(sp500['Close'])
y_predykcja = np.full_like(y_test, fill_value=y_mean)

bląd_kwadratowy = mean_squared_error(y_test, y_predykcja)
R2 = r2_score(y_test, y_predykcja)
