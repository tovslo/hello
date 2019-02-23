from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .forms import UserForm
from .models import Person

def index(request):
    header = "Personal Data"  # обычная переменная
    langs = ["English", "German", "Spanish"]  # массив
    user = {"name": "Tom", "age": 23}  # словарь
    addr = ("Абрикосовая", 23, 45)  # кортеж

    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return TemplateResponse(request, "index.html", data)

def about(request):
    return HttpResponse("<h2>О сайте</h2>")
 
def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

#форма
def form(request):
    if request.method == "POST":
        # Валидация нан стороне сервера:
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            #name = request.POST.get("name")
            age = userform.cleaned_data["age"]
            #age = request.POST.get("age")
            comment = userform.cleaned_data["comment"]
            #comment = request.POST.get("comment")#
            email = request.POST.get("email")
            return HttpResponse("<h2>Hello, {0}! You're already {1}!</h2><p>email: {3}</p><p>Какая-то фигня:</br>{2}</p><h1><a href='/'>Домой</a></h1>".format(name, age, comment, email))

        else:
            return HttpResponse("Invalid data")
    else:
        userform = UserForm()

        return render(request, "firstapp/templates/form.html", {"form": userform})


# получение данных из бд
def getDB(request):
    people = Person.objects.all()
    return render(request, "firstapp/templates/getdb.html", {"people": people})


# сохранение данных в бд
def setDB(request):
    if request.method == "POST":
        tom = Person()
        tom.name = request.POST.get("name")
        tom.age = request.POST.get("age")
        tom.save()
    return HttpResponseRedirect("/getdb/")


# изменение данных в бд
def editDB(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/getdb/")
        else:
            return render(request, "firstapp/templates/editdb.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def deleteDB(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/getdb/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")