from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    # url(r'^api/account/create$',
    #     views.create_account,
    #     name='account_creation',)
    path('fetch_users/', views.fetch_users),
    path('create_user/', views.create_user),
]