From python:3.9-alpine
RUN pip install flask
RUN apt-get install apache2 -y
WORKDIR /myapp
COPY main.py /myapp/main.py
CMD ["python", "/myapp/main.py"]
