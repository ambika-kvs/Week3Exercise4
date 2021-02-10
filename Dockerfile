FROM python:3.9-slim
COPY . /src
RUN pip install flask
CMD ["python", "/src/hello.py"]
