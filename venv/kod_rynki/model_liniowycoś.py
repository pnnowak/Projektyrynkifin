import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

#bezsensowny model, bo sp500['Close'] to prawie samo co sp500['Open']
sp500 = yf.download('^GSPC', start='2000-01-01', end='2025-01-01')
X_train, X_test, y_train, y_test = train_test_split(sp500['Open'], sp500['Close'], test_size=0.2, random_state=123)

model = LinearRegression()
model.fit(X_train, y_train)

y_predykcja = model.predict(X_test)
blad_kwadratowy = mean_squared_error(y_test, y_predykcja)
R2 = r2_score(y_test, y_predykcja)
print(f"Pierwszy model z testowym mse:455.98301456751824 r2: 0.9997088304136665")
print(f"Mse: {blad_kwadratowy}")
print(f"R2: {R2}")

plt.scatter(X_test, y_test, color="blue", label="Prawdziwe dane")
plt.plot(X_test, y_predykcja, color="red", label="Regresja liniowa")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()
