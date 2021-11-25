FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/meongj/MySecondDjangoApp_Pinterest.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

#RUN echo "SECRET_KEY=" > .env
RUN pip install gunicorn

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "pragmatic.wsgi", "--bind", "0.0.0.0:8000"]

