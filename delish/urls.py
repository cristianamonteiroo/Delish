from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from product.views import *
from core.views import *

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('shop/', product, name='product'),
    path('shop/<slug:slug>/', produit_filter, name='produit_filter'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='cart'),
    path('update_item/', updateItem, name='update_item'),
    path('faq/', faq, name='faq'),
    path('contact/', contact, name='contact'),
    path('about-me/', aboutme, name='about-me'),
    
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
