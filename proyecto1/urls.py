"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from proyecto1.views import base, index,login_view,logout_view,register_view,about

from django.conf import settings
from django.conf.urls.static import static

from users.views import Detail_user_profile, Update_user_profile


urlpatterns = [
    path('admin/', admin.site.urls),
    path("base/",base, name="base"),
    path("peliculas/", include("peliculas.urls")),
    path("", index, name="inicio"),
    path("auth/login/",login_view, name="login"),
    path("logout/",logout_view, name="logout"),
    path("auth/register/",register_view, name="register"),
    path('users/', include('users.urls')),
    path("about/",about,name="about"),
    path('user/update_user_profile/<int:pk>/', Update_user_profile.as_view(), name = 'update_user_profile'),
    path('user/detail_user_profile/<int:pk>/', Detail_user_profile.as_view(), name = 'detail_user_profile'),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
