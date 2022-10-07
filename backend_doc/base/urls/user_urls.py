from django.urls import path
from ..views import user_views as views


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.registerUser, name = 'register'),
    path("profile/", views.getUserProfile, name="user-profile"),
    path("profile/update/", views.updateUserProfile, name="user-profile-update"),
    path(" ", views.getUsers, name="users"),

]
# http://127.0.0.1:8000/api/users/profile/update/
