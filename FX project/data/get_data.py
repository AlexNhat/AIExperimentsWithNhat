# Tổng quan bước này ta lấy dữ liệu từ mt5
# Sau đó lưu vào biến tên là data_forex
# Và nhớ khai báo các cặp tiền tệ cần thiết vào biến symbols

import requests
import pandas as pd
from datetime import datetime


def get_history(symbol: str, timeframe: str = "D1", start: str = "2014-01-01", end: str = datetime.now().date().isoformat()):
    """
    Retrieves historical data for a given financial symbol within a specified timeframe.

    Parameters:
    - symbol (str): The financial symbol for which historical data is requested.
    - timeframe (str, optional): The timeframe of historical data (default: "D1" for daily).
    - start (str, optional): The start date for the historical data in the format "YYYY-MM-DD" (default: "2014-01-01").
    - end (str, optional): The end date for the historical data in the format "YYYY-MM-DD" (default: current date).

    Returns:
    - pandas.DataFrame: A DataFrame containing historical data with columns like 'Open', 'High', 'Low', 'Close', etc.
                        The DataFrame is indexed by the 'Date' column, representing the timestamp of each data point.
    """

    # Construct parameters for the API request
    params = {
        "timeframe": timeframe,
        "start": start,
        "end": end,
    }

    # Make a request to the historical data API
    response = requests.get(f"http://221.132.33.180:8005/history/{symbol}", params=params)
    response.raise_for_status()

    # Convert the response to a DataFrame and format the 'Date' column
    data = response.json()
    data = pd.DataFrame(data)
    data["Date"] = pd.to_datetime(data['Date'], unit='s')
    data.set_index("Date", inplace=True)

    return data


def get_data(symbols):
    """
    Hàm này nhận danh sách các biểu tượng (symbols) và lấy dữ liệu lịch sử cho từng biểu tượng.

    Parameters:
    - symbols (dict): Danh sách các biểu tượng cần lấy dữ liệu, được đưa vào dưới dạng dictionary.

    Returns:
    - data_forex (dict): Dictionary chứa dữ liệu lịch sử cho từng biểu tượng. Mỗi khóa của dictionary là một biểu tượng,
      và mỗi giá trị là dữ liệu lịch sử tương ứng của biểu tượng đó.
    """
    data_forex = {}

    # Lặp qua danh sách biểu tượng
    for sym in symbols["all"]:
        # Gọi hàm get_history để lấy dữ liệu lịch sử cho biểu tượng hiện tại
        data_forex[sym] = get_history(sym)

        # In ra biểu tượng đang được xử lý (optional)
        print(sym)

    # Trả về dictionary chứa dữ liệu lịch sử cho tất cả các biểu tượng
    return data_forex
