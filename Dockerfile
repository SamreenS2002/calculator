FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# This line below is the most important—it copies 'templates', 'app.py', everything!
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]