from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from radflix import views

urlpatterns = [
    url(r'^api/radies$', views.movie_list),
    url(r'^api-token-auth$', obtain_auth_token),
]