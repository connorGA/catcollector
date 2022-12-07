from django.shortcuts import render
from django.http import HttpResponse
# import Cat model thats connected to the Database
from .models import Cat, Dog
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

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

# add these lines to the imports at the top
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
# DOGS
class DogCreate(CreateView):
  model = Dog
  fields = '__all__'
  success_url = '/'

# CATS
class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  success_url = '/cats'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect('/cats')

class CatUpdate(UpdateView):
  model = Cat
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/cats/' + str(self.object.pk))

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats'

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

def profile(request, username):
  user = User.objects.get(username=username)
  cats = list(Cat.objects.filter(user=user))

  return render(request, 'profile.html', { 'username': username, 'cats': cats})
  

def login_view(request):
     # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
    else: # it was a get request so send the emtpy login form
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})  