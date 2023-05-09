
from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('second/', secondpage, name="secondpage"),
    path('new/', new, name="new"), #빈칸이 있는 사이트
    path('create/', create, name="create"), #적어서 저장하는 사이트
    path('<int:id>', detail,name="detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]