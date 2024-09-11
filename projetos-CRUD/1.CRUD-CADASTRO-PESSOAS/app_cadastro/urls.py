from django.urls import path
from app_cadastro import views

urlpatterns = [
    path("",  views.home, name="home"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("update/<int:id_usuario>", views.update, name='update'),
    path("editado/<int:id_usuario>", views.editado, name="editado"),
    path("deletar;<int:id_usuario>", views.deletar, name="deletar")

]


