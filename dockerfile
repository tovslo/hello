#  Контейнер, запускающий проект hello под django dev server
# собрать:      docker build . -t hello
# запустить:    docker run -p 8000:8000 hello 

# пляшем от питона
FROM python:3.6.3

# рабочая директория в контетйнере
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src/hello

# установка зависимостей в контейнере
RUN pip3 install django

# копируем проект в директорию контейнера
COPY . /opt/services/djangoapp/src

# пробрасываем порт из контейнера
EXPOSE 8000

# команда, запускаемая в котнейнере
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
