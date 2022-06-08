
from django.urls import path
from .views import index, create_post, update_post,delete_post

urlpatterns = [
        path("",index, name="index"),
        path("create_post/", create_post, name="create_post"),
        path("update_post/<int:id>", update_post, name="update_post"),
        path("delete_post/<int:id>", delete_post, name="delete_post"),
    ]
