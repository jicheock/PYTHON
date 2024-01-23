
import yfinance

apple=yfinance.Ticker("AAPL")
current_price=apple.info['currentPrice']
print(f"애플 주식의 현재 가격:{current_price}")
microsoft=yfinance.Ticker("MSFT")
current_price=microsoft.info['currentPrice']
print(f"마이크로소프트의 현재 가격:{current_price}")