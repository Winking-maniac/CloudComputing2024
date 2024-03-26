FROM python:3.11

RUN python3.11 -m pip install flask
RUN python3.11 -m pip install mysql-connector-python
RUN python3.11 -m pip install cryptography
COPY ./app.py ./app.py
CMD ["flask",  "--app", "app", "run", "-h", "0.0.0.0"]
