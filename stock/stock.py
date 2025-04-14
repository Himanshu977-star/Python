import threading  # For running multiple stock trackers concurrently
import yfinance as yf  # To fetch stock data from Yahoo Finance
import time  # To manage time delays and timestamps

# Function to fetch and log the stock price continuously
def get_stock_price(stock_symbol):
    while True:
        try:
            # Create a Ticker object for the given stock symbol
            stock = yf.Ticker(stock_symbol)
            
            # Get the current market price
            price = stock.info.get("regularMarketPrice", "N/A")

            # Print the stock symbol and its current price
            print(f"{stock_symbol}: ${price}")

            # Log the price to a file with a timestamp
            with open("stock_prices.txt", "a") as file:
                file.write(f"{time.ctime()} - {stock_symbol}: ${price}\n")

        except Exception as e:
            # Print any errors that occur while fetching stock data
            print(f"Error fetching {stock_symbol}: {e}")
        
        # Wait for 5 seconds before fetching the price again
        time.sleep(5)

# List of stock symbols to track
stocks = ["AAPL", "TSLA", "GOOGL", "MSFT"]

# Creating and starting threads for each stock symbol
threads = []
for stock in stocks:
    # A new thread is created to run get_stock_price(stock) independently
    thread = threading.Thread(target=get_stock_price, args=(stock,))
    
    # daemon=True allows threads to stop automatically when the main program exits
    thread.daemon = True
    
    # Threads are added to the list and started
    threads.append(thread)
    thread.start()

# Keep the main thread alive to allow background threads to continue running
try:
    while True:
        time.sleep(1)  # Sleep to reduce CPU usage
except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    print("Stopped tracking.")
