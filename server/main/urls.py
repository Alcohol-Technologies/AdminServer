from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('update_schedule', views.update_schedule, name='schedule'),
    #path('/upload', views.upload_file, name='upload')
]