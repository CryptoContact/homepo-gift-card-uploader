FROM python:3

ADD . /


RUN pip install wheel
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install celery

CMD ["gunicorn", "--bind", "0.0.0.0:5100", "app:app"]
