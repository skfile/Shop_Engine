from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('store/', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about")
    # path('search/<str:pk>', views.search, name="search")
]
