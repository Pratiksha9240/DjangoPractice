from django.urls import path
from . import views

urlpatterns = [
    # use name in the redirect function
    path('',views.login_user,name='login'),
    path('signup',views.signup),
    path('logout',views.logout),

]