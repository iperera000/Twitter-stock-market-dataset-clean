import pandas as pd
import matplotlib.pyplot as plt

#load dataset
df = pd.read_csv("data/Twitter_stockmarket_dataset.csv")
df.head()

#rename columns
df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")

#covert 'date' to datetime
df['date'] = pd.to_datetime(df['date'], errors ='coerce')

#drop rows with missing values
df = df.dropna()

#reset index
df = df.reset_index(drop=True)


#convert volume to integer
df['volume'] = df['volume'].astype(int)


#save cleaned dataset
df.to_csv("output/Twitter_stock_cleaned.csv", index=False)
print("Cleaned dataset saved!")

#report 1 - Closing price over time
plt.figure(figsize=(12,6))
plt.plot(df['date'], df['close'], label='close price', color='green')
plt.title('Twitter stock close price over time')
plt.xlabel('date')
plt.ylabel('close price ($)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("output/close_price.png")
plt.close()


#report 2 - High-Low range over time
plt.figure(figsize=(12,6))
plt.plot(df['date'], df['high'], label='high', color='blue')
plt.plot(df['date'], df['low'], label='low', color='red')
plt.fill_between(df['date'], df['low'], df['high'], color='purple', alpha=0.3)
plt.title('Twitter stock high-low range')
plt.xlabel('date')
plt.ylabel('price ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("output/High-Low_range.png")
plt.close()

print("All reports saved in the output folder")