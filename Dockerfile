# Sử dụng Python 3.10 làm base image
FROM python:3.10

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép toàn bộ project vào container
COPY . .

# Cập nhật pip và cài đặt các thư viện cần thiết
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Thiết lập biến môi trường cho Flask
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Mở cổng 5000 cho Flask
EXPOSE 5000

# Chạy ứng dụng bằng Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
