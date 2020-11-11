from django.urls import path, include

from . import views
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', firstPage, name='home'),
    path('signup/', signup, name='Signup'),
    path('login/', login_request, name='Login'),
    path('logout/', auth_views.LogoutView.as_view(), name='Logout'),
    path('second/', secondPage, name='Page_2'),
    path('addMovie/', addMovies, name='addMovie'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)