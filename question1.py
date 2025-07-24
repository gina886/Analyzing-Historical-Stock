import yfinance as yf
import pandas as pd

# download tesla stock data
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")

# reset index to have a clean datafram
tesla_data.reset_index(inplace=True)

# display the fiest few rows of the dataframe
print(tesla_data.head())