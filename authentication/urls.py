from django.urls import path
from authentication.views import signup, login_view, logout_view

urlpatterns = [
    path('', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
