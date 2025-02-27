import pandas as pd
import numpy as np

def basic_summary(data):
    """
    Tóm tắt cơ bản về dữ liệu.

    Parameters:
    - data (DataFrame): Dữ liệu cần được mô tả.

    Returns:
    - summary (DataFrame): DataFrame chứa các thông tin tóm tắt cơ bản về dữ liệu.
      Các cột bao gồm:
        - `Column`: Tên của các cột trong DataFrame.
        - `Unique Values`: Số lượng giá trị duy nhất trong mỗi cột.
        - `Missing Values`: Số lượng giá trị thiếu trong mỗi cột.
        - `Min`: Giá trị nhỏ nhất trong mỗi cột.
        - `25th Percentile`: Phần trăm 25 nhất (Q1) của mỗi cột.
        - `Mean`: Giá trị trung bình của mỗi cột.
        - `Median`: Giá trị trung vị (Q2) của mỗi cột.
        - `75th Percentile`: Phần trăm 75 nhất (Q3) của mỗi cột.
        - `Max`: Giá trị lớn nhất trong mỗi cột.
    """
    summary = pd.DataFrame()
    summary['Column'] = data.columns
    summary['Unique Values'] = data.nunique().values
    summary['Missing Values'] = data.isnull().sum().values
    summary['Min'] = data.min().values
    summary['25th Percentile'] = data.quantile(0.25).values
    summary['Mean'] = data.mean().values
    summary['Median'] = data.median().values
    summary['75th Percentile'] = data.quantile(0.75).values
    summary['Max'] = data.max().values
    return summary


def numerical_summary(data):
    """
    Tóm tắt cho dữ liệu kiểu số.

    Parameters:
    - data (DataFrame): Dữ liệu cần được mô tả.

    Returns:
    - summary (DataFrame): DataFrame chứa các thông tin tóm tắt về các cột kiểu số.
      Các cột bao gồm:
        - `Column`: Tên của các cột trong DataFrame.
        - `Unique Values`: Số lượng giá trị duy nhất trong mỗi cột.
        - `Missing Values`: Số lượng giá trị thiếu trong mỗi cột.
        - `Min`: Giá trị nhỏ nhất trong mỗi cột.
        - `25th Percentile`: Phần trăm 25 nhất (Q1) của mỗi cột.
        - `Mean`: Giá trị trung bình của mỗi cột.
        - `Median`: Giá trị trung vị (Q2) của mỗi cột.
        - `75th Percentile`: Phần trăm 75 nhất (Q3) của mỗi cột.
        - `Max`: Giá trị lớn nhất trong mỗi cột.
        - `Standard Deviation`: Độ lệch chuẩn của mỗi cột.
    """
    summary = pd.DataFrame()
    summary['Column'] = data.columns
    summary['Unique Values'] = data.nunique().values
    summary['Missing Values'] = data.isnull().sum().values
    summary['Min'] = data.min().values
    summary['25th Percentile'] = data.quantile(0.25).values
    summary['Mean'] = data.mean().values
    summary['Median'] = data.median().values
    summary['75th Percentile'] = data.quantile(0.75).values
    summary['Max'] = data.max().values
    summary['Standard Deviation'] = data.std().values
    return summary

def correlation_matrix(data):
    """
    Ma trận tương quan giữa các biến số.

    Parameters:
    - data (DataFrame): Dữ liệu cần được mô tả.

    Returns:
    - correlation (DataFrame): Ma trận tương quan giữa các biến số.
    """
    return data.corr()

def describe_data(data):
    """
    Tổng hợp tất cả các hàm mô tả dữ liệu.

    Parameters:
    - data (DataFrame): Dữ liệu cần được mô tả.

    Returns:
    - summary (DataFrame): Tổng hợp thông tin tóm tắt từ các hàm mô tả dữ liệu.
    """
    summary = pd.DataFrame()

    if data.empty:
        return summary

    # Tóm tắt cơ bản
    basic = basic_summary(data)
    summary = pd.concat([summary, basic], axis=1)

    # Tóm tắt dữ liệu kiểu số
    numerical_cols = data.select_dtypes(include=np.number).columns
    numerical = numerical_summary(data[numerical_cols])
    summary = pd.concat([summary, numerical], axis=1)

    # Ma trận tương quan
    correlation = correlation_matrix(data)
    summary = pd.concat([summary, correlation], axis=1)

    return summary
