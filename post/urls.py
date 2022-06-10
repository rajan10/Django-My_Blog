
from django.urls import path
from .views import index, create_post, update_post,delete_post, detail_post, update_comment,delete_comment

urlpatterns = [
        path("",index, name="index"),
        path("create_post/", create_post, name="create_post"),
        path("update_post/<int:id>", update_post, name="update_post"),
        path("delete_post/<int:id>", delete_post, name="delete_post"),
        path("detail_post/<int:id>", detail_post, name="detail_post"),



        # path("create_comment/<int:id>", create_comment, name="create_comment"),
        path("update_comment/<int:id>", update_comment, name="update_comment"),
        path("delete_comment/<int:id>", delete_comment, name="delete_comment"),

]
