FROM python:3
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENV PYTHONPATH /app
CMD ["python3", "src/main.py"]