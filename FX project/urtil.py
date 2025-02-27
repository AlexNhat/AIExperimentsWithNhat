# Tổng quan bước này ta lấy dữ liệu từ mt5
# Sau đó lưu vào biến tên là data_forex
# Và nhớ khai báo các cặp tiền tệ cần thiết vào biến symbols

import requests
import pandas as pd
from datetime import datetime

"""Cảnh báo không được thay đổi địa chỉ ip của hàm này"""
def get_history(symbol: str, timeframe: str = "D1", start: str = "2016-01-01", end: str = datetime.now().date().isoformat()):
    params = {
        "timeframe": timeframe,
        "start": start,
        "end": end,
    }
    response = requests.get(f"http://221.132.33.180:8005/history/{symbol}", params=params)
    response.raise_for_status()
    data = response.json()
    data = pd.DataFrame(data)
    data["Date"] = pd.to_datetime(data['Date'], unit='s')
    data.set_index("Date", inplace=True)
    return data

# Phía trên là hàm lấy dữ liệu từ mt5  và đầu vào là cạp tiền tệ của forex, crypto, stock
# hàm trả về data của symbols đó

# symbols = {'all': ["EURCHF", "EURNZD", "NZDUSD", "AUDNZD", "USDJPY", "NZDJPY", "GBPJPY", "USDCHF"]}
symbols = {'all': ["EURCHF"]}
"""Đoạn code này có thể chỉnh sửa lấy loại tiền tệ theo yêu cầu"""
def get_data(symbols):
  data_forex = {}
  for sym in symbols["all"]:
    data_forex[sym] = get_history(sym)
    print(sym)
  return data_forex

data_forex = get_data(symbols)
print(data_forex)