from django import forms

class CategoryForm(forms.Form):
    YEARS = [x for x in range(1900, 2005)]

    FIRST_NAME = forms.CharField(max_length = 50)
    LAST_NAME = forms.CharField(max_length=50)
    BIRTH_DATE = forms.DateField(required=True,widget=forms.SelectDateWidget(years=YEARS))
    EMAIL = forms.EmailField()