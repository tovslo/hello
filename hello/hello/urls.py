from django.urls import path
from django.views.generic import TemplateView
from firstapp import views
from django.conf.urls import url
from django.contrib import admin

langs = ["English", "German", "French", "Spanish", "Chinese"]
data = {"n": 5}
header = "О сайте"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('form/', views.form),
    path('setdb/', views.setDB),
    path('getdb/', views.getDB),
    path('getdb/create/', views.setDB),
    path('editdb/<int:id>', views.editDB),
    path('deletedb/<int:id>', views.deleteDB),
    path('about/', TemplateView.as_view(template_name="firstapp/templates/about.html")),
    path('contact/', TemplateView.as_view(template_name="firstapp/templates/contacts.html")),
    path('', TemplateView.as_view(template_name="firstapp/templates/index.html",
                                        extra_context={"header": header, "langs": langs, "data": data}))
]

