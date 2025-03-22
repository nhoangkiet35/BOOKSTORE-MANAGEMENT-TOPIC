# 🚀 Hướng dẫn Deploy Flask + MySQL lên Railway  

Railway là nền tảng hosting miễn phí và dễ dàng để deploy ứng dụng Flask + MySQL. Dưới đây là hướng dẫn chi tiết.  

---

## 1️⃣ **Cài đặt các công cụ cần thiết**  

🔹 **Git** (để đẩy code lên GitHub)  
🔹 **Python 3.10** (Railway chỉ hỗ trợ tối đa 3.10)  
🔹 **Pipenv hoặc Virtualenv** (để quản lý môi trường ảo)  
🔹 **Railway CLI** (hỗ trợ deploy dễ dàng)  

👉 **Cài đặt Railway CLI:**  

```sh
npm i -g @railway/cli
```

---

## 2️⃣ **Chuẩn bị Project Flask**  

📂 **Cấu trúc thư mục:**

```
BOOKSTORE-MANAGEMENT-TOPIC/
│── bookstore/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│── config.py
│── requirements.txt
│── run.py
│── Procfile
│── .env
│── Dockerfile (tùy chọn)
```

---

## 3️⃣ **Cấu hình `requirements.txt`**  

📌 Chạy lệnh sau để tạo:  

```sh
pip freeze > requirements.txt
```

📌 Đảm bảo file này có các package quan trọng:

```
flask
flask-sqlalchemy
flask-migrate
gunicorn
pymysql
```

---

## 4️⃣ **Cấu hình `Procfile` (chạy Flask trên Railway)**  

Tạo file **Procfile** (không có đuôi `.txt`) với nội dung:  

```
web: gunicorn -w 4 -b 0.0.0.0:$PORT run:app
```

---

## 5️⃣ **Cấu hình `config.py` để kết nối MySQL**  

🔹 Railway sẽ cung cấp biến môi trường `DATABASE_URL`, sửa `config.py`:  

```python
import os
from urllib.parse import quote

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mysql+pymysql://root:password@localhost:3306/bookstore")
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

---

## 6️⃣ **Đưa Code Lên GitHub**  

```sh
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/bookstore.git
git push -u origin main
```

---

## 7️⃣ **Deploy lên Railway**  

🔹 **Bước 1:** Đăng nhập Railway  

```sh
railway login
```

🔹 **Bước 2:** Tạo project Railway  

```sh
railway init
```

🔹 **Bước 3:** Kết nối đến GitHub  

- Vào [Railway.app](https://railway.app/)  
- Chọn **New Project** > **Deploy from GitHub**  
- Chọn repository của bạn  
- Railway sẽ tự động deploy 🎉  

---

## 8️⃣ **Thêm Database MySQL trên Railway**  

🔹 **Bước 1:** Truy cập [Railway](https://railway.app/)  
🔹 **Bước 2:** Chọn **Add Plugin > MySQL**  
🔹 **Bước 3:** Railway sẽ tạo database và hiển thị `DATABASE_URL`  
🔹 **Bước 4:** Cập nhật biến môi trường  

- Vào **Settings > Environment**  
- Thêm biến `DATABASE_URL` với giá trị từ Railway  

---

## 9️⃣ **Chạy Migration (Tạo Bảng Database)**  

```sh
railway run flask db init
railway run flask db migrate -m "Initial migration"
railway run flask db upgrade
```

---

## 🔥 **Hoàn tất!** 🎉  

✅ **Flask + MySQL đã deploy thành công trên Railway!**  
Bạn có thể truy cập API bằng đường link từ Railway.  

Nếu gặp lỗi gì, cứ hỏi mình nhé! 🚀
