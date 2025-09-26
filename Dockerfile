# 使用官方 Python 基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码
COPY . .

# 暴露端口（比如 Flask 默认 5000）
EXPOSE 5000

# 启动命令（app.py 里要有 if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)）
CMD ["python", "app.py"]
