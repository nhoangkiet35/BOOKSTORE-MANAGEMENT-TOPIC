# Hướng dẫn cài đặt Locust

## 1. Giới thiệu

Locust là một công cụ kiểm thử tải mã nguồn mở, sử dụng Python để mô phỏng hàng ngàn người dùng đồng thời gửi yêu cầu đến hệ thống của bạn nhằm đánh giá hiệu suất.

Locust là 1 công cụ kiểm thử hiệu suất (load testing) mã nguồn mở sử dụng HTTP và một vài giao thức khác.

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
    wait_time = between(1, 3)  # Thời gian chờ giữa các yêu cầu

    @task
    def load_test(self):
        self.client.get("/")
```

### 4.2. Chạy Locust

Chạy lệnh sau trong thư mục chứa `locustfile.py`:

```sh
locust
```

Sau đó, truy cập vào giao diện web của Locust tại [http://localhost:8089](http://localhost:8089) để bắt đầu kiểm thử tải.

## 5. Tùy chọn nâng cao

### 5.1. Chạy kiểm thử từ dòng lệnh

Có thể chạy kiểm thử mà không cần giao diện web:

```sh
locust --headless -u 10 -r 2 -t 1m --host=http://example.com
```

Trong đó:

- `-u 10`: 10 người dùng ảo
- `-r 2`: 2 người dùng được khởi tạo mỗi giây
- `-t 1m`: Chạy trong 1 phút
- `--host=http://example.com`: Địa chỉ website cần kiểm thử

### 5.2. Chạy kiểm thử trên nhiều máy chủ

Locust hỗ trợ chạy kiểm thử phân tán bằng cách sử dụng master và worker:

- Chạy **master**:

  ```sh
  locust --master
  ```

- Chạy **worker**:

  ```sh
  locust --worker --master-host=<IP của master>
  ```

## 6. Kết luận

Locust là một công cụ mạnh mẽ để kiểm thử hiệu suất hệ thống, dễ dàng mở rộng và tích hợp vào CI/CD. Bạn có thể tham khảo thêm tài liệu chính thức tại [https://locust.io](https://locust.io).
