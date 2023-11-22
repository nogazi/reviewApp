from django.urls import path
from .views import home_view, about_us_view, contact_us_view, product_list_view, register_view, login_view, profile_view, add_product_view
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', home_view, name='home'),
    path('about-us/', about_us_view, name='about_us'),
    path('contact-us/', contact_us_view, name='contact_us'),
    path('product-list/', product_list_view, name='product_list'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_product/', add_product_view, name='add_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)