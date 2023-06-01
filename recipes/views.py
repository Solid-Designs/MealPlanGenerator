from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe
from .plan_generator import generate_plan

# Create your views here.


def index(request):
    # Put them in a comma seperated list
    raw_plan = generate_plan()
    return render(request, 'recipes/index.html', {'raw_plan': raw_plan})
