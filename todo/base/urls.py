from unicodedata import name
from django.urls import path
from .views import CustomLoginView, RegisterPage, TaskCreate, TaskDelete, TaskDetail, TaskList, TaskUpdate
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name = 'tasks'),
    path('task/details/<str:pk>/', TaskDetail.as_view(), name = 'details'),
    path('create/', TaskCreate.as_view(), name = 'create'),
    path('update/<str:pk>/', TaskUpdate.as_view(), name='update'),
    path('delete/<str:pk>/', TaskDelete.as_view(), name= 'delete'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name= 'logout'),
]