import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from ladowaniedata import ladowanie_data

sp500 = ladowanie_data()
correlation_matrix_spearman = sp500.corr(method='spearman')
print(correlation_matrix_spearman)
correlation_matrix = sp500.corr()
print(correlation_matrix)

sp5001 = pd.DataFrame()

# SMA (Simple Moving Average)
sp5001['SMA'] = sp500['Close'].rolling(window=16).mean()
# EMA (Exponential Moving Average)
sp5001['EMA_5'] = sp500['Close'].ewm(span=16, adjust=False).mean()

# MACD (Moving Average Convergence Divergence)
sp5001['EMA_12'] = sp500['Close'].ewm(span=12, adjust=False).mean()
sp5001['EMA_26'] = sp500['Close'].ewm(span=26, adjust=False).mean()

# MACD jako różnica EMA
sp5001['MACD'] = sp5001['EMA_12'] - sp5001['EMA_26']

# Linia sygnału jako EMA z MACD (np. 9-dniowa)
sp5001['Signal'] = sp5001['MACD'].ewm(span=9, adjust=False).mean()

print(sp5001)