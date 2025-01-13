import yfinance as yf
import pandas as pd
import pandas_ta as ta
import numpy as np

# Step 1: Fetch Historical Data
def fetch_data(symbol, start_date, end_date):
    try:
        data = yf.download(symbol, start=start_date, end=end_date, interval="1h")
        if data.empty:
            raise ValueError("No data fetched. Please check the symbol and date range.")
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Step 2: Calculate Stochastic RSI
def calculate_stochrsi(data, period=14):
    try:
        data["stochrsi"] = ta.stochrsi(data["Close"], length=period)
        if data["stochrsi"].isnull().all():
            raise ValueError("StochRSI calculation resulted in all NaN values.")
        return data
    except Exception as e:
        print(f"Error calculating StochRSI: {e}")
        return None

# Step 3: Implement Trading Strategy
def backtest_strategy(data):
    wins = 0
    results = []

    # Drop rows with NaN values in the stochrsi column
    data = data.dropna(subset=["stochrsi"])

    for i in range(1, len(data)):
        current = data.iloc[i]
        previous = data.iloc[i - 1]
        result = {"stochrsi": current["stochrsi"], "price": current["Close"], "win": "Loss"}

        # Condition 1: StochRSI > 95 and price is greater than a past StochRSI < 5
        if current["stochrsi"] > 95:
            past_low = data[data["stochrsi"] < 5]
            if not past_low.empty:
                past_low_price = past_low["Close"].iloc[-1]
                if current["Close"] > past_low_price:
                    wins += 1
                    result["win"] = "Win"

        # Condition 2: StochRSI < 5 and price is lower than a past StochRSI > 95
        elif current["stochrsi"] < 5:
            past_high = data[data["stochrsi"] > 95]
            if not past_high.empty:
                past_high_price = past_high["Close"].iloc[-1]
                if current["Close"] < past_high_price:
                    wins += 1
                    result["win"] = "Win"

        results.append(result)

    results_df = pd.DataFrame(results)
    return wins, results_df

# Main
if __name__ == "__main__":
    symbol = "^NDX"  # US100
    start_date = "2024-10-01"
    end_date = "2025-01-01"

    data = fetch_data(symbol, start_date, end_date)
    if data is not None:
        data = calculate_stochrsi(data)
        if data is not None:
            wins, results_df = backtest_strategy(data)
            print(f"Number of wins: {wins}")

            # Save the results to an Excel file
            results_df.to_excel('US100_backtest_results.xlsx', index=False)
            print("Results saved to US100_backtest_results.xlsx")
        else:
            print("StochRSI calculation failed.")
    else:
        print("Data fetching failed.")
