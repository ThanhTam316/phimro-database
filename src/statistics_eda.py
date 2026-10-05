"""Phần II: Thống kê mô tả và tìm phim có giá trị cực trị."""


def calculate_basic_stats(df):
    """Tính trung bình, trung vị và độ lệch chuẩn của các cột số.

    Tham số:
        df (pandas.DataFrame): Dữ liệu phim đã làm sạch.

    Trả về khi hoàn thiện:
        pandas.DataFrame: Mỗi hàng ứng với một cột số; các cột kết quả
        là Mean, Median và Std; chỉ mục mang tên column.

    Công việc cần triển khai:
        - Chọn cột số có ý nghĩa phân tích, không dùng mã định danh phim.
        - Tính Mean, Median và Std mẫu (ddof=1), bỏ qua giá trị thiếu.
        - Giữ giá trị thiếu nếu không đủ quan sát để tính thống kê.
        - Xử lý đầu vào rỗng hoặc không có cột số một cách nhất quán.
        - Trả về bảng; tầng gọi lưu data/results2.csv với index=True
          để giữ tên các cột được thống kê.
    """
    pass


def get_top_bottom_movies(df, column, top_n=3):
    """Tìm tất cả phim có giá trị lớn nhất và nhỏ nhất trong một cột.

    Tham số:
        df (pandas.DataFrame): Dữ liệu phim đã làm sạch.
        column (str): Tên cột số cần tìm cực trị.
        top_n (int): Số phim lấy ở mỗi đầu bảng, mặc định là 3.

    Trả về khi hoàn thiện:
        tuple[pandas.DataFrame, pandas.DataFrame]: Hai bảng gồm top_n phim
        theo thứ tự (điểm cao nhất, điểm thấp nhất), có cột Title và column.

    Công việc cần triển khai:
        - Kiểm tra cột tồn tại và có kiểu số; bỏ qua giá trị thiếu.
        - Dùng .nlargest(top_n, column) và .nsmallest(top_n, column).
        - Nếu không có giá trị hợp lệ, trả về hai bảng rỗng cùng cấu trúc.
        - Không sửa đổi DataFrame đầu vào.
    """
    pass