import matplotlib.pyplot as plt
import numpy as np
from ladowaniedata import ladowanie_data


sp500 = ladowanie_data()
# Wyświetlenie kilku pierwszych wierszy
print(sp500.head())
print(sp500.index)
#

print(sp500.describe())
print(sp500.isnull().sum())

plt.figure(figsize=(12, 6))
# sp500['Log_Returns'] = np.log(sp500['Close'] / sp500['Close'].shift(1))
# sp500['Returns'] = sp500['Close'].pct_change(periods=360)
sp500_resampled = sp500.resample('30D').mean()
sp500['Logclose'] = np.log(sp500_resampled['Close']/sp500_resampled['Close'].shift(1))
plt.subplot(1, 2, 1)
plt.scatter(sp500.index, sp500['Logclose'], label="Zmiany procentowe", color="blue", alpha=0.7)
plt.subplot(1, 2, 2)
plt.plot(sp500_resampled['Close'], label="Cena", color="black", alpha=0.7)
plt.show()