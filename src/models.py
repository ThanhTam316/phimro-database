"""Phần III và IV: Phân cụm, giảm chiều và dự đoán doanh thu phim."""


def run_kmeans_clustering(df, n_clusters):
    """Phân cụm phim bằng K-means trên các đặc trưng số đã chuẩn hóa.

    Tham số:
        df (pandas.DataFrame): Dữ liệu phim đã làm sạch.
        n_clusters (int): Số cụm, từ 1 đến số mẫu hợp lệ.

    Trả về khi hoàn thiện:
        pandas.DataFrame: Bản sao dữ liệu có thêm cột cluster.

    Công việc cần triển khai:
        - Thống nhất danh sách đặc trưng; loại mã phim và nhãn cụm cũ.
        - Kiểm tra số cụm, dữ liệu rỗng và số mẫu phân biệt khả dụng.
        - Xử lý giá trị thiếu, vô hạn và chuẩn hóa bằng StandardScaler.
        - Dùng sklearn.cluster.KMeans; đặt random_state và n_init rõ ràng
          để kết quả có thể tái lập.
        - Gắn nhãn đúng chỉ mục ban đầu; quy định cách biểu diễn các hàng
          không thể phân cụm và không thay đổi dữ liệu đầu vào.
    """
    pass


def run_pca_reduction(df):
    """Giảm đặc trưng phim xuống hai chiều để trực quan hóa.

    Tham số:
        df (pandas.DataFrame): Dữ liệu phim, có thể chứa nhãn cluster.

    Trả về khi hoàn thiện:
        pandas.DataFrame: Tọa độ PC1 và PC2, giữ chỉ mục của mẫu hợp lệ.

    Công việc cần triển khai:
        - Chọn đặc trưng số tương ứng với bước phân cụm; loại mã phim
          và cột cluster để nhãn cụm không trở thành đặc trưng.
        - Xử lý giá trị thiếu, vô hạn và chuẩn hóa các đặc trưng.
        - Kiểm tra có ít nhất hai mẫu và hai đặc trưng khả dụng.
        - Dùng sklearn.decomposition.PCA với n_components=2.
        - Giữ liên kết chỉ mục để ghép tọa độ với tên phim và nhãn cụm;
          xem xét tỷ lệ phương sai giải thích khi diễn giải biểu đồ.
    """
    pass


def train_revenue_prediction_model(df):
    """Huấn luyện mô hình hồi quy để dự đoán doanh thu phòng vé.

    Tham số:
        df (pandas.DataFrame): Dữ liệu có doanh thu mục tiêu và đặc trưng.

    Trả về khi hoàn thiện:
        sklearn.pipeline.Pipeline: Bộ tiền xử lý và mô hình đã huấn luyện,
        hỗ trợ predict trên bảng đặc trưng có cùng cấu trúc đầu vào.

    Công việc cần triển khai:
        - Ánh xạ cột doanh thu thực tế sang biến mục tiêu; thống nhất đơn vị.
        - Loại hàng thiếu mục tiêu; chọn đặc trưng có sẵn tại lúc dự đoán,
          không dùng doanh thu hoặc thông tin phát sinh từ doanh thu.
        - Chia tập huấn luyện/kiểm tra trước khi học bước tiền xử lý;
          đặt random_state để tái lập và kiểm tra số mẫu tối thiểu.
        - Dùng Pipeline và ColumnTransformer để điền khuyết, mã hóa cột
          phân loại và chuẩn hóa khi cần; chỉ fit trên tập huấn luyện.
        - Chọn LinearRegression hoặc RandomForestRegressor.
        - Đánh giá MAE, RMSE và R² trên tập kiểm tra; ghi nhận kết quả
          phục vụ báo cáo, rồi trả về Pipeline đã huấn luyện.
    """
    pass