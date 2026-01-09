from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .forms import ReviewForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .api import search_movies_api, search_moviesByID
import requests

# Create your views here.
def hello(request):
    return render(request, 'index.html')
class hello2(View):
    def get(self,request):
        return HttpResponse("hello world from class")

def home(request):
    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    return render(request, 'review_in.html', {'form':form})

#  for login page
def LogIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # get authenticated user
            login(request, user)
            return redirect('index')  # or redirect('home')
    else:
        form = AuthenticationForm()  # empty form for GET request

    return render(request, 'login.html', {'form': form})
# for creating an account
def account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()   # creates user
            login(request, user) # logs user in
            return redirect('log')
    else:
        form = UserCreationForm()

    return render(request, 'newAccount.html', {'form': form})
# searches movie by id 
def view_movies(request, movie_id):
    
    try:
        movie = search_moviesByID(movie_id)
        
    except Exception as e:
        return HttpResponse("Movie does not exist")
    
    return render(request, 'movies.html',{
        
        
        "movie": movie,
        })
# search page
def search_page(request):
    
    
    return render(request, 'search.html')



# searches movies
def search_movies(request):
    query = request.GET.get("q", "").strip()
    params = {
        "api_key": settings.API_KEY,
        "query": query,
        "language": "en-US"
    }
    if not query:
        
        return JsonResponse({"results": []})
    try:
        data = search_movies_api(query,params)
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"results": [], "error": str(e)})
