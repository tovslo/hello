#  Контейнер, запускающий проект hello под uwsgi для nginx
# собрать:      docker build . -t hello-uwsgi-nginx
# запустить:    docker run -p 8001:8001 hello-uwsgi-nginx 

# пляшем от питона
FROM python:3.6.3

# рабочая директория в контетйнере
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

# установка зависимостей в контейнере
# we use --system flag because we don't need an extra virtualenv
COPY Pipfile Pipfile.lock /opt/services/djangoapp/src/
RUN pip install pipenv && pipenv install --system

WORKDIR /opt/services/djangoapp/src/hello

# копируем проект в директорию контейнера
COPY . /opt/services/djangoapp/src

# пробрасываем порт из контейнера
EXPOSE 8000

# команда, запускаемая в котнейнере
CMD ["uwsgi", "--ini", "uwsgi.ini"]
#CMD ["bash"]
