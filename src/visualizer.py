"""Phần II và III: Tạo biểu đồ Matplotlib để hiển thị trên Streamlit."""


def plot_histogram(df, column):
    """Tạo biểu đồ phân phối của một cột số.

    Tham số:
        df (pandas.DataFrame): Dữ liệu phim đã làm sạch.
        column (str): Tên cột số cần trực quan hóa.

    Trả về khi hoàn thiện:
        matplotlib.figure.Figure: Hình để tầng giao diện dùng st.pyplot.

    Công việc cần triển khai:
        - Kiểm tra cột tồn tại, có kiểu số và còn giá trị hợp lệ.
        - Bỏ giá trị thiếu hoặc vô hạn, chọn số khoảng chia phù hợp.
        - Tạo Figure/Axes riêng bằng matplotlib.pyplot.subplots.
        - Vẽ histogram với tiêu đề, tên trục và đơn vị rõ ràng.
        - Trả về Figure, không gọi plt.show hoặc hàm Streamlit tại đây;
          tầng gọi chịu trách nhiệm đóng hình sau khi sử dụng.
    """
    pass


def plot_radar_chart(df, movie1_name, movie2_name):
    """So sánh đặc trưng của hai phim trên biểu đồ radar.

    Tham số:
        df (pandas.DataFrame): Dữ liệu có tên phim và các đặc trưng số.
        movie1_name (str): Tên phim thứ nhất.
        movie2_name (str): Tên phim thứ hai.

    Trả về khi hoàn thiện:
        matplotlib.figure.Figure: Biểu đồ radar so sánh hai phim.

    Công việc cần triển khai:
        - Thống nhất cột tên phim; báo lỗi nếu không tìm thấy hoặc trùng
          tên nhiều bản ghi, yêu cầu phân biệt bằng năm phát hành/mã phim.
        - Chọn ít nhất ba đặc trưng số có ý nghĩa; xử lý giá trị thiếu.
        - Chuẩn hóa về cùng thang đo dựa trên tập dữ liệu tham chiếu,
          không chỉ hai phim; xử lý riêng đặc trưng có giá trị hằng.
        - Tạo trục cực, khép kín các đa giác, thêm nhãn và chú giải;
          ghi rõ các giá trị hiển thị đã được chuẩn hóa.
        - Trả về Figure, không gọi plt.show hoặc sửa dữ liệu đầu vào;
          tầng gọi đóng hình sau khi hiển thị.
    """
    pass