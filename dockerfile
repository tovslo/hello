#  Контейнер, запускающий проект hello под gunicorn
#  !!! НЕ РАЗДАЕТ СТАТИКУ !!!
# собрать:      docker build . -t hello-gunicorn
# запустить:    docker run -p 8000:8000 hello-gunicorn 

# пляшем от питона
FROM python:3.6.3

# рабочая директория в контетйнере
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src/hello

# установка зависимостей в контейнере
RUN pip3 install django gunicorn

# копируем проект в директорию контейнера
COPY . /opt/services/djangoapp/src

# пробрасываем порт из контейнера
EXPOSE 8000

# команда, запускаемая в котнейнере
CMD ["gunicorn", "--bind", ":8000", "hello.wsgi:application"]
