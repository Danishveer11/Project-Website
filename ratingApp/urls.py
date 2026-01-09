from django.urls import path
from . import views

urlpatterns = [
    path('function',views.hello, name='index'),
    path('class',views.hello2.as_view()),
    path('review', views.home, name='postReview'),
    path('login', views.LogIn, name='log'),
    path('account', views.account, name='create_account'),
    path('movies/<int:movie_id>/', views.view_movies, name='movies_view'),
    path('search/', views.search_page, name='search_page'),
    path('search/api/', views.search_movies, name='search_movies')

]
