
import pandas as pd
import numpy as np
from finta import TA


# Hàm khởi tạo các  technical indicator
def create_indicators(ohlcv: pd.DataFrame) -> pd.DataFrame:
    """
       Generates technical indicators based on the provided OHLCV (Open-High-Low-Close-Volume) DataFrame.

       Parameters:
       - ohlcv (pd.DataFrame): A DataFrame containing historical OHLCV data.

       Returns:
       - pd.DataFrame: A modified DataFrame with additional columns representing various technical indicators.

       The function calculates and adds commonly used technical indicators to the input DataFrame, such as Moving Averages,
       Relative Strength Index (RSI), Moving Average Convergence Divergence (MACD), and any other relevant indicators.
       The modified DataFrame includes these additional indicator columns, providing valuable insights for technical analysis.
       """

    data = ohlcv.copy()
    indi, signal = bias(ohlcv)
    data = pd.concat([data, indi], axis=1)
    data['BIAS_signal'] = signal
    data['VR'], data["VR_signal"] = vr(ohlcv)
    data['TRIX'], data["TRIX_signal"] = trix(ohlcv)
    data['ER'] = TA.ER(ohlcv)
    data['EVWMA'] = TA.EVWMA(ohlcv)
    data['VWAP'] = TA.VWAP(ohlcv)
    data['MOM'] = TA.MOM(ohlcv)
    data['ROC'] = TA.ROC(ohlcv)
    data['RSI'] = TA.RSI(ohlcv)
    data['IFT_RSI'] = TA.IFT_RSI(ohlcv)
    data['ATR'] = TA.ATR(ohlcv)
    data['BBWIDTH'] = TA.BBWIDTH(ohlcv)
    data['ADX'] = TA.ADX(ohlcv)
    data['STOCH'] = TA.STOCH(ohlcv)
    data['STOCHD'] = TA.STOCHD(ohlcv)
    data['AO'] = TA.AO(ohlcv)
    data['MI'] = TA.MI(ohlcv)
    data['MFI'] = TA.MFI(ohlcv)
    data['PZO'] = TA.PZO(ohlcv)
    data['EFI'] = TA.EFI(ohlcv)
    data['EMV'] = TA.EMV(ohlcv)
    data['CCI'] = TA.CCI(ohlcv)
    data['FISH'] = TA.FISH(ohlcv)
    data['FVE'] = TA.FVE(ohlcv)

    macd = TA.MACD(ohlcv)
    data['MACDCal'] = macd['MACD'] - macd['SIGNAL']

    macdev = TA.EV_MACD(ohlcv)
    data['EVMACD'] = macdev["MACD"]

    data['TR'] = TA.TR(ohlcv)

    DMI = TA.DMI(ohlcv)
    data['DMI+'] = DMI["DI+"]
    data['DMI-'] = DMI["DI-"]

    VORTEX = TA.VORTEX(ohlcv)
    data['VIp'] = VORTEX["VIp"]
    data['ADL'] = TA.ADL(data)

    TSI = TA.TSI(ohlcv)
    data['TSI'] = TSI["TSI"]
    data['TSIsignal'] = TSI["signal"]

    KST = TA.KST(ohlcv)
    data['KST'] = KST["KST"]

    data['CHAIKIN'] = TA.CHAIKIN(ohlcv)
    data['OBV'] = TA.OBV(ohlcv)
    data['WOBV'] = TA.WOBV(ohlcv)

    EBBP = TA.EBBP(ohlcv)
    data['EBBPBull'] = EBBP["Bull."]
    data['EBBPBear'] = EBBP["Bear."]

    BASPN = TA.BASPN(ohlcv)
    data['BASPNBuy'] = BASPN["Buy."]
    data['BASPNSell'] = BASPN["Sell."]
    data['COPP'] = TA.COPP(ohlcv)

    BASP = TA.BASP(ohlcv)
    data['BASPBuy'] = BASP["Buy."]
    data['BASPSell'] = BASP["Sell."]

    WTO = TA.WTO(ohlcv)
    data['WTOWT1'] = WTO["WT1."]

    data['STC'] = TA.STC(ohlcv)
    data['VPT'] = TA.VPT(ohlcv)

    # Có 50 kỹ thuật technical indicators ở đây
    return data

LOOK_BACK = 10
"""Hàm này dùng để phân chia data ra theo từng ngày nối đuôi nhau vựa trên lock_back"""
# Xem xem trung bình 10 ngày tăng hay giảm, là dùng để xem xu hướng của tiền

def create_dataset(data, label, look_back=10):  #
    X_ = []
    y_ = []
    # Tạo vòng lạp để lấy các lookback
    for i in range(len(data)-look_back-1):
        X_.append(data[i:(i+look_back)])
        y_.append(label[i + look_back])
    return np.array(X_), np.array(y_)

""" Hàm này để lấy các ngày liên tiếp theo n_days để làm các cột dữ liệu"""

def add_past_days_as_feature(data: pd.DataFrame, n_days: int = 5):
    data = pd.concat([data.shift(i).add_suffix(f"_{i}") for i in range(n_days)], axis=1)
    return data

" Hàm Bias dùng để so sánh giữ hai hai tính hiệu dài hạn và ngắn hạn vựa trên short_val và long_val "
def bias(prices):
    short_avg = prices['Close'].rolling(3, min_periods=1).mean()
    long_avg = prices['Close'].rolling(5, min_periods=1).mean()

    short_val = pd.Series(((prices['Close'] - short_avg) / short_avg) * 100, name="BIAS_short", index=prices.index)
    long_val = pd.Series(((prices['Close'] - long_avg) / long_avg) * 100, name="BIAS_long", index=prices.index)
    indi = pd.concat([short_val, long_val], axis=1)

    # So sánh xem dài hạn hay ngắn hạn cái nào sẽ lời hơn
    signal = pd.Series((long_val > short_val).astype(int), name="BIAS_signal", index=prices.index)
    return indi, signal

def vr(prices):
    maximum = (prices['High'] + prices['Close'].shift(1).bfill()).mean() # Lấy giá cao nhất ngày hiện tạo cộng cho ngày đóng cửa của tương lai,
    # Nếu tương lai là Nan thì cộng cho giá đóng cưa hiện tại
    minimum = (prices['Low'] + prices['Close'].shift(1).bfill()).mean()
    high = prices['High'].rolling(14, min_periods=1).mean()
    low = prices['Low'].rolling(14, min_periods=1).mean()

    # Tính chỉ số
    indi = pd.Series((maximum - minimum) / (high - low), name="VR", index=prices.index)
    signal = pd.Series((indi > 0.5).astype(int), name="VR_signal", index=prices.index)
    return indi, signal

# Hàm tính giá trị Trix
def trix(prices):
    indi = TA.TRIX(prices, 10)
    signal = pd.Series((indi < 0).astype(int), name="TRIX_signal", index=prices.index)
    return indi, signal