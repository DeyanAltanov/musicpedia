from django.urls import path

from musicpedia.accounts.views import login_user, logout_user, RegisterView

urlpatterns = (
    path('login/', login_user, name='log in user'),
    path('logout/', logout_user, name='log out user'),
    path('register/', RegisterView.as_view(), name='register user'),
)