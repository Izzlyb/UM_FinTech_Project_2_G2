import pandas as pd

growth_stock = ['PANW', 'LRCW', 'AAPL', 'AMZN', 'MSFT', 'TSLA', 'CAT', 'DE']
cyclical_stocks = ['DIS', 'EXPE', 'NUE', 'DPZ', 'CMG']
aggressive_stocks = ['TSLA', 'MSTR', 'FANG', 'CROX', 'AMD', 'NVDA', 'ALGN']
conservative_stocks = ['KO', 'CI', 'PG', 'UNH', 'HD', 'CAT', 'LMT', 'XOM', 'CAH' ]

stock_portfolio = ['Balanced',  'Aggressive', 'Conservative', 'Growth', 'Dividend']

etfs_growth = ['IWY', 'VONG', 'SPGP', 'MGK', 'SPYG', 'SCHG']
etf_balance = ['AOA', 'OAK', 'PSMB', 'GAL', 'BND', 'NOBL']
etf_dividends = ['HDV', 'VYM', 'SPHD','SCHD','SPYD', 'VYMI', 'VIG' ]

portfolios = ["", "Hybrid Portfolio", "Portfolio 2023", "Stocks Portfolio", "ETF Portfolio"]

# "Ticker", "OriginalPrice", "TickerQuantity", "OriginalDate", "ActualPrice", "TransactionType"
PortfolioAssets = pd.DataFrame(
    columns = ("Ticker", "Original Price", "Ticker Quantity", "Original Date", "Actual Price")
)

# PortfoliosOwned = {
#     "Hybrid Portfolio" : HybridPortfolio, 
#     "Portfolio 2023" : Portfolio2023, 
#     "ETF Portfolio" : PortfolioETF, 
#     "Stocks Portfolio" : PortfolioStocks
# }
