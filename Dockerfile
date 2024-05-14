FROM python:3.8.0
RUN mkdir /app
WORKDIR /app/
ADD . /app/
RUN pip3 install -r requirements.txt
ENV FLASK_APP=/app/app.py
CMD ["flask", "run"]

