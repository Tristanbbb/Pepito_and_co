FROM python:3
WORKDIR .
COPY . .
RUN pip install -r requirements.txt
ENV PYTHONPATH .
CMD ["python3", "src/main.py"]