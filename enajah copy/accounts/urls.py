from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name="accounts"
urlpatterns=[
    path("login/", views.custom_login,name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="accounts/logout.html"),name="logout"),
    path("register/", views.register ,name="register"),
    path("profile/<username>/", views.profile ,name="profile"),
    path("profile/<username>/update/", views.edit_profile ,name="edit"),
    path("<username>/pay/<palier_slug>", views.enroll_student ,name="enroll_student"),
    path("users/", views.users ,name="users"),
]
