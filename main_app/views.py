from django.shortcuts import render
from django.http import HttpResponse
# import Cat model thats connected to the Database
from .models import Cat

# temp add Cats class
# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

#     def __str__(self):
#         return f"{self.name}"

# cats = [
#     Cat('Rufus', 'tabbycat', 'crazy cat', 103),
#     Cat('Simba', 'lion', 'brave', 5),
#     Cat('Garfield', 'tabbycat', 'likes lasagna', 43)
# ]

# Create your views here.
def index(request):
    cats = list(Cat.objects.all())
    return render(request, 'index.html', { 'cats': cats})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def cats_index(request):
    cats = list(Cat.objects.all())
    return render(request, 'cats/index.html', { 'cats': cats })

def cats_show(request, cat_id):
    cat =Cat.objects.get(id=cat_id)
    return render(request, 'cats/show.html', { 'cat': cat })
