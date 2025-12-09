from django.urls import path
from api.views import user_views as views

urlpatterns = [
    path('register/', views.registerUser, name="register"),
    path('profile/', views.getUserProfile, name="user-profile"),
    path('profile/update/', views.updateUserProfile, name="user-profile-update"),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('delete/<str:pk>/', views.deleteUser, name="user-delete"),
]