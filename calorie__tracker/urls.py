from django.urls import path

from .views import HomePageView,LoginPage,LogOutPage, ProfilePage,RegisterPage, add_food, delete_food, select_food, update_food

urlpatterns = [
	path('', HomePageView,name='home'),
	path('login/',LoginPage,name='login'),
	path('logout/',LogOutPage,name='logout'),
	path('register/',RegisterPage,name='register'),
	path('profile/',ProfilePage,name='profile'),
	path('add_food/',add_food,name='add_food'),
	path('update_food/<str:pk>/',update_food,name='update_food'),
	path('delete_food/<str:pk>/',delete_food,name='delete_food'),
    path('select_food/',select_food,name='select_food'),
]