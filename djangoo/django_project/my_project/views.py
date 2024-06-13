from django.shortcuts import render
from .models import Owner, Pet

def main_page(request):
    data = Pet.objects.all()

    context = {
        "data": data,
    }

    return render(request, 'main.html', context)


