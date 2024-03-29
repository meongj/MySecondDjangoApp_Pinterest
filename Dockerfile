FROM python:3.9.0

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/meongj/MySecondDjangoApp_Pinterest.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

#RUN echo "SECRET_KEY=" > .env
RUN pip install gunicorn

RUN pip install mysqlclient

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]

