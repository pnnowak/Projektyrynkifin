import yfinance as yf


sp500 = yf.download('^GSPC', start='2000-01-01', end='2025-01-01')


def ladowanie_data():
    return sp500
