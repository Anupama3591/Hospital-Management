
from django.urls import path
from . import views

urlpatterns = [  
    path("",views.index,name="index"),
    path("about/",views.about, name="about"),
    path("contact/",views.contact, name="contact"),
    path("add/",views.add,name="add"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('delete/<int:id>/', views.delete,name="deletedata"),
    path('update/<int:id>/', views.update,name="update"), 
]