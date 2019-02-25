from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    # url(r'^api/account/create$',
    #     views.create_account,
    #     name='account_creation',)
    path('users/create', views.UserList.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]