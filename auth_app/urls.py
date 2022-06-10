
from .views import register,Login, Logout


from django.urls import path, include

urlpatterns = [

    path('register/',register, name="register"),
    path('login/', Login, name="login"),
    path('logout/', Logout, name="logout"),

]
