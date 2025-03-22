# Hướng dẫn cài đặt Locust

## 1. Giới thiệu

Locust là một công cụ kiểm thử tải mã nguồn mở, sử dụng Python để mô phỏng hàng ngàn người dùng đồng thời gửi yêu cầu đến hệ thống của bạn nhằm đánh giá hiệu suất.

Locust là một công cụ load testing mã nguồn mở dựa trên Python, giúp bạn kiểm tra hiệu suất của API hoặc website bằng cách mô phỏng nhiều người dùng đồng thời gửi request đến hệ thống.

Locust test có thể sử dụng bởi cả công cụ dòng lệnh hoặc giao diện Web thân thiện, dễ tiếp cận. Các thông số như thông lượng (throughput), thời gian phản hồi (response times) và các lỗi (errors) có thể được xem trực tiếp theo thời gian thực, hoặc/và được export ra để phân tích sau.

## 2. Yêu cầu hệ thống

- Python 3.7 trở lên
- pip (Python package manager)

## 3. Cài đặt

### 3.1. Cài đặt Python (nếu chưa có)

- **Windows**: Tải Python từ trang chủ: [https://www.python.org/downloads/](https://www.python.org/downloads/) và cài đặt.
- **Linux/macOS**: Cài đặt Python bằng trình quản lý gói:

  ```sh
  sudo apt update && sudo apt install python3 python3-pip  # Ubuntu/Debian
  brew install python  # macOS
  ```

### 3.2. Cài đặt Locust

Sử dụng pip để cài đặt Locust:

```sh
pip install locust
```

Kiểm tra cài đặt thành công:

```sh
locust --version
```

## 4. Cách sử dụng cơ bản

### 4.1. Tạo file kiểm thử `locustfile.py`

Tạo một file Python `locustfile.py` và thêm đoạn code sau:

```python
from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Khoảng thời gian chờ giữa các request

    @task
    def get_homepage(self):
        self.client.get("/")  # Gửi request GET đến trang chủ

    @task
    def get_about_page(self):
        self.client.get("/about")  # Gửi request GET đến trang /about
```

Trong đó:

- `HttpUser`: Định nghĩa một lớp người dùng thực hiện các yêu cầu HTTP.
- `task`: Đánh dấu một phương thức là một nhiệm vụ mà người dùng sẽ thực hiện.
- `wait_time`: Xác định khoảng thời gian chờ ngẫu nhiên giữa các request để mô phỏng người dùng thực tế.

### 4.2. Chạy Load Test với Locust

Chạy lệnh sau trong thư mục chứa `locustfile.py`:

```sh
locust
```

Sau đó, truy cập vào giao diện web của Locust tại [http://localhost:8089](http://localhost:8089) để bắt đầu kiểm thử tải.

## 5. Tùy chọn nâng cao

### 5.1. Chạy kiểm thử từ dòng lệnh

Nếu muốn chạy test mà không cần giao diện web, bạn có thể dùng lệnh sau:

```sh
locust --headless -u 10 -r 2 -t 1m --host=http://example.com
```

Trong đó:

- `-u 10`: Số lượng user ảo (virtual users).
- `-r 2`: Số user được tạo mỗi giây.
- `-t 1m`: Chạy load test trong 1 phút.
- `--host=http://example.com`: Địa chỉ website cần kiểm thử

### 5.2. Chạy kiểm thử trên nhiều máy chủ (Load Test Phân Tán)

Nếu bạn muốn chạy load test trên nhiều máy để mô phỏng số lượng lớn user hơn, bạn có thể dùng chế độ master-worker:

- Chạy **master**:

  ```sh
  locust --master
  ```

- Chạy **worker** (trên các máy khác nhau):

  ```sh
  locust --worker --master-host=<IP của master>
  ```

### 5.3. Mở rộng Locust Test

Bạn có thể mở rộng bài test bằng cách thêm nhiều endpoint, gửi dữ liệu POST, hoặc thêm logic phức tạp hơn.

Ví dụ gửi request POST:

```python
    @task
    def create_user(self):
        self.client.post("/users", json={"name": "John", "email": "john@example.com"})
```

## 6. Phân tích kết quả

Sau khi chạy load test, Locust sẽ hiển thị các thông số quan trọng như:

- Tổng số request được gửi.
- Thời gian phản hồi trung bình.
- Số request bị lỗi.
- Tỷ lệ request thành công/thất bại.

Nếu chạy test từ giao diện web, bạn có thể xem chi tiết các số liệu và tải xuống báo cáo.

## 7. Kết luận

Locust là một công cụ mạnh mẽ để kiểm thử hiệu suất hệ thống, dễ dàng mở rộng và tích hợp vào CI/CD. Bạn có thể tham khảo thêm tài liệu chính thức tại [https://locust.io](https://locust.io).
