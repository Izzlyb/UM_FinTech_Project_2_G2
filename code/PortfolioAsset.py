# "Ticker", "Tkr_Quantity", "Actual Price", "Buy_Qty", "Buy Price", "Buy Date", "Sell_Qty", "Sold Price", "Sell Date"

import pandas as pd

class PortfolioAsset():
    def __init__(self, trk, price, qty=0, date="", act_price=0.0):
        self.Ticker = trk,
        self.OriginalPrice = price,
        self.Quantity = qty,
        self.OriginalDate = date,
        self.ActualPrice = act_price,
        self.TransType = '-'
        
    # def __str__(self):
    #     self.Ticker, 
    #     self.OriginalPrice,
    #     self.Quantity,
    #     self.OriginalDate,
    #     self.ActualPrice


def CreatePortfolioDf(portfl):
    df = pd.DataFrame()

    row_list = []
    for i in range(len(portfl)):
        data1 = [portfl[i].Ticker,
                 portfl[i].OriginalPrice,
                 portfl[i].Quantity,
                 portfl[i].OriginalDate,
                 portfl[i].ActualPrice
                 ]
        
        row_list.append(data1)
    
    df = pd.DataFrame(
        data = row_list, 
        columns = ("Ticker", "Original Price", "Ticker Quantity", "Original Date", "Actual Price")
    )
    
    return df


# "Ticker", "OriginalPrice", "TickerQuantity", "OriginalDate", "ActualPrice", "TransactionType"
# "Ticker", "BuyPrice", "BuyQuantity", "BuyDate", "ActualPrice", "TransactionType"
# "Ticker", "Sold Price", "SellQuantity", "SellDate", "ActualPrice", "TransactionType"

PortfolioStocks = [
    PortfolioAsset("AAPL", 191.00, 100, "2022-12-15", 0.0),
    PortfolioAsset("HD", 310.55, 120, "2022-05-15", 0.0),
    PortfolioAsset("PG", 152.50, 180, "2022-05-15", 0.0),
    PortfolioAsset("AMT", 195.04, 110, "2022-05-15", 0.0),
    PortfolioAsset("FDX", 247.55, 190, "2022-05-15", 0.0),
    PortfolioAsset("JPM", 146.76, 200, "2022-05-15", 0.0),
    PortfolioAsset("MRNA", 121.73, 140, "2022-05-15", 0.0),
    PortfolioAsset("XOM", 107.46, 210, "2022-05-15", 0.0),
    PortfolioAsset("APD", 297.07, 120, "2022-05-15", 0.0),
    PortfolioAsset("NFLX", 440.90, 100, "2022-05-15", 0.0),
    PortfolioAsset("AWK", 143.97, 175, "2022-05-15", 0.0)
]


PortfolioETF = [
    PortfolioAsset("SCHD", 191.00, 100, "2022-12-15", 0.0),
    PortfolioAsset("SPAB", 310.55, 120, "2022-05-15", 0.0),
    PortfolioAsset("TLT", 152.50, 180, "2022-05-15", 0.0),
    PortfolioAsset("VGT", 195.04, 110, "2022-05-15", 0.0),
    PortfolioAsset("IWM", 247.55, 190, "2022-05-15", 0.0)
]


Portfolio2023 = [
    PortfolioAsset("MSFT", 191.00, 15, "2022-12-15", 0.0),
    PortfolioAsset("ABNG", 132.35, 10, "2022-05-15", 0.0),
    PortfolioAsset("MA", 393.96, 25, "2022-05-15", 0.0),
    PortfolioAsset("CRM", 211.65, 35, "2022-05-15", 0.0),
    PortfolioAsset("DE", 406.48, 5, "2022-05-15", 0.0),
    PortfolioAsset("LMT", 406.48, 5, "2022-05-15", 0.0),
    PortfolioAsset("NOW", 562.87, 5, "2022-05-15", 0.0),
    PortfolioAsset("UNP", 206.13, 5, "2022-05-15", 0.0),
    PortfolioAsset("SNPS", 434.01, 5, "2022-05-15", 0.0),
    PortfolioAsset("SPY", 191.00, 20, "2022-12-15", 0.0),
    PortfolioAsset("QQQ", 370.10, 10, "2022-05-15", 0.0),
    PortfolioAsset("SCHG", 74.96, 15, "2022-05-15", 0.0),
    PortfolioAsset("SMH", 153.60, 30, "2022-05-15", 0.0),
    PortfolioAsset("DGROW", 51.70, 70, "2022-05-15", 0.0),
    PortfolioAsset("SLV", 51.70, 65, "2022-05-15", 0.0)
]


HybridPortfolio = [
    PortfolioAsset("NVDA", 424.13, 100, "2022-12-15", 0.0),
    PortfolioAsset("WMT", 310.55, 120, "2022-05-15", 0.0),
    PortfolioAsset("JNJ", 152.50, 180, "2022-05-15", 0.0),
    PortfolioAsset("CAT", 247.55, 190, "2022-05-15", 0.0),
    PortfolioAsset("AMT", 195.04, 110, "2022-05-15", 0.0),
    PortfolioAsset("CRWD", 195.04, 110, "2022-05-15", 0.0),
    PortfolioAsset("BIL", 91.47, 190, "2022-05-15", 0.0),
    PortfolioAsset("VOO", 91.47, 190, "2022-05-15", 0.0),    
    PortfolioAsset("GLD", 178.47, 190, "2022-05-15", 0.0)   
]


PortfoliosOwned = {}

PortfoliosOwned = dict({
    "Hybrid Portfolio" : HybridPortfolio, 
    "Portfolio 2023" : Portfolio2023, 
    "ETF Portfolio" : PortfolioETF, 
    "Stocks Portfolio" : PortfolioStocks
})


# etfs_growth = ['IWY', 'VONG', 'SPGP', 'MGK', 'SPYG', 'SCHG']
# etf_balance = ['AOA', 'OAK', 'PSMB', 'GAL', 'BND', 'NOBL']
# etf_dividends = ['HDV', 'VYM', 'SPHD','SCHD','SPYD', 'VYMI', 'VIG' ]
