from django.urls import path

from . import views

urlpatterns = [
    path('', views.Login),
    path('SignUp',views.Signup),
    path('SignIn',views.Login),
    path('features',views.About),
    path('logout',views.logout),
    path('mymethod',views.home),
    path('email_3',views.email_1),

]