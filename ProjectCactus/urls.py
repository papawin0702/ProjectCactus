"""ProjectCactus URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from ProjectCactus import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cart/', views.cart_view, name="cart"),
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.log),
    path('', views.displaystore),
    path('shopall/', views.displayproduct),
    path('story/', views.story),
    path('about/', views.about),
    path('help/', views.help),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_registration.api.urls')),
    path('store/', include('store.urls')),
    path('product/', include('product.urls'))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

