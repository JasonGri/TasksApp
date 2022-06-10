from django.urls import path
from tasks import views

app_name = 'tasks' #namespace error if you forget this

urlpatterns = [
    path('add/', views.add, name='add'),
    path('', views.index, name='index'),
]


