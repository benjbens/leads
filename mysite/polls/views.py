from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import CategoryForm
from .models import Name

# Create your views here.
def get_name(request):
    context = {
        'page_title' : "Landing page",
    }
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['FIRST_NAME']
            last_name = form.cleaned_data['LAST_NAME']
            birth_date = form.cleaned_data['BIRTH_DATE']
            email = form.cleaned_data['EMAIL']

            print(first_name)

            new_name = Name(first_name=first_name,last_name=last_name,birth_date=birth_date,email=email)
            new_name.save()

            print(first_name)
            context['form'] = CategoryForm()
            return render(request, 'landing.html', context)
    else:
        context['form'] = CategoryForm()
    return render(request, 'landing.html', context)


def show_data(request):
    context = {'all': Name.objects.all(), 'form': CategoryForm()}
    return render(request, 'show.html', context)





