FROM python:3.7
RUN mkdir /app
WORKDIR /app/
RUN python -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"
ADD . /app/
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ENV PATH="/opt/venv/bin:$PATH"
COPY . /app/
CMD ["python", "/app/app.py"]

