from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    # url(r'^api/account/create$',
    #     views.create_account,
    #     name='account_creation',)
    path('fetch_users/', views.fetch_users),
    path('create_user/', views.create_user),
    path('update_user/<int:user_id>', views.update_user),
    path('delete_user/<int:user_id>', views.delete_user),
    path('fetch_user/<int:user_id>', views.fetch_user),
]