from django import forms

class CategoryForm(forms.Form):
    FIRST_NAME = forms.CharField(max_length = 50)
    LAST_NAME = forms.CharField(max_length=50)
    BIRTH_DATE = forms.DateField(required=True,widget=forms.SelectDateWidget())
    EMAIL = forms.EmailField()