from django import forms


class UserForm(forms.Form):
    # метка, начальное значение, виджет не по умолчанию, порядок полей, подсказка
    name = forms.CharField(label="Имя:", initial="Tovslo", help_text="Введите имя", widget=forms.TextInput(attrs={"class": "myfield"}))
    age = forms.IntegerField(label="Возраст:", initial=48, help_text="Введите возраст")
    comment = forms.CharField(label="Комментарий:", widget=forms.Textarea, help_text="Какую-нить фигню", required=False)
    email = forms.EmailField(required=False, min_length=7)
    field_order = ["comment", "name", "age", "email"]
    required_css_class = "field"
    error_css_class = "error"

