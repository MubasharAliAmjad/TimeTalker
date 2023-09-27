from django.urls import path
from .views import Registration, SignIn, Profile, Dashboard
from .import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('', Registration.as_view(), name='registration'),
    path('signin', SignIn.as_view(), name='signin'),
    path('profile', Profile.as_view(), name='profile'),
    path('dashboard', Dashboard.as_view(), name="dashboard"),
    path('displayroom/<str:pk>', views.displayroom, name="displayroom"),
 
    # login-section
    path("auth/login/", LoginView.as_view
         (template_name="chat/LoginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]

