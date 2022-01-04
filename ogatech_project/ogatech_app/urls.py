from django.urls import path
from ogatech_app import views


app_name = 'ogatech_app'

urlpatterns = [
    # path('', views.index, name='index' ),
    path('register/',views.register,name="register"),
    path('user_login/',views.user_login,name="user_login"),
    path('pricing/',views.pricing,name="pricing"),
]