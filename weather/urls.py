from django.urls import path
from . import views

urlpatterns = [
	path('get_current_weather/<str:zip_code>/<str:country_code>/', views.get_current_weather),

]