import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV files
tcs = pd.read_csv("D:\TCS_stock_history2021.csv")

# Handle missing or null values by filling with zeros
tcs['Open'].fillna(0, inplace=True)
tcs['Close'].fillna(0, inplace=True)

# Print the first few rows of the DataFrame
print(tcs.head())

# Create separate line charts to visualize the "Open" and "Close" values
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(tcs['Open'], label='Open', color='blue')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.title('TCS Stock Open Price History')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(tcs['Close'], label='Close', color='red')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('TCS Stock Close Price History')
plt.legend()
plt.grid(True)

plt.tight_layout()  # Ensures proper spacing between subplots
plt.show()

