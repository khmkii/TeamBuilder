from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'profile/(?P<slug>[-\w]+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'profile/(?P<slug>[-\w]+)/edit/$', views.EditProfileView.as_view(), name='edit_profile'),
    url(r'login/$', views.LoginView.as_view(), name='login'),
    url(r'logout/$', views.LogOutView.as_view(), name='logout'),
    url(r'signup/$', views.SignUpView.as_view(), name='sign_up'),
]
