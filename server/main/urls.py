from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('update_schedule', views.update_schedule, name='schedule'),
    path('show_users', views.show_users, name='users')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)