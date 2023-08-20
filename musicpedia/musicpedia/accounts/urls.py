from django.urls import path

from musicpedia.accounts.views import login_user, logout_user, RegisterView, profile_details, user_details

urlpatterns = (
    path('login/', login_user, name='log in user'),
    path('logout/', logout_user, name='log out user'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('profile_details/', profile_details, name='profile details'),
    path('user_details/<int:pk>', user_details, name='user details')
)