# Используем официальный образ Python
FROM python:3.9-slim

# Копируем исходный код приложения
COPY . /app
WORKDIR /app

# Устанавливаем зависимости с помощью setup.py
RUN pip install --no-cache-dir .

# Опционально: устанавливаем переменные среды
#ENV PYTHONUNBUFFERED=1

# Опционально: запускаем приложение
CMD ["python", "main.py"]
