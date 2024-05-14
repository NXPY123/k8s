FROM python:3.8.0
RUN mkdir /app
WORKDIR /app/
ADD . /
RUN pip3 install -r requirements.txt
CMD ["python", "/app/app.py"]

