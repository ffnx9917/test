# 使用官方 Python 映像
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 複製當前目錄下的所有內容到容器中的 /app 目錄
COPY . /app

# 安裝所需的依賴項
RUN pip install -r requirements.txt

# 執行 Python 程式
CMD ["python", "app.py"]