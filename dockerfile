#  Контейнер, запускающий проект hello под uwsgi
# собрать:      docker build . -t hello-uwsgi
# запустить:    docker run -p 8000:8000 hello-uwsgi 

# пляшем от питона
FROM python:3.6.3

# рабочая директория в контетйнере
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src/hello

# установка зависимостей в контейнере
RUN pip3 install django uwsgi

# копируем проект в директорию контейнера
COPY . /opt/services/djangoapp/src

# пробрасываем порт из контейнера
EXPOSE 8000

# команда, запускаемая в котнейнере
CMD ["uwsgi", "--ini", "uwsgi.ini"]
