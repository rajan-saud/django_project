from django.urls import path
from . import views

urlpatterns = [
	# homepage view
	path('', views.home, name = 'home'),

	# login view
	path('login/', views.login, name = 'login')	
]