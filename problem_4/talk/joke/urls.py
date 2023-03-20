from django.urls import path
from . import views


app_name = 'joke'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('add/',views.addView, name='addView'),
    path('entry/<int:id>/', views.entry_view, name='entry_view'),
]