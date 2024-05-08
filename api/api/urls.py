from django.contrib import admin
from django.urls import include, path
from accounts.views import UserViewset, RegisterAPI, LoginAPI, UserAPI, ChangePasswordView, LogoutAPI
from other.views import PostViewset, SessionViewset, SetupViewset
from knox import views as knox_views
from rest_framework import routers

router = routers.DefaultRouter()
# admin viewsets
router.register(r'accounts', UserViewset)
router.register(r'posts', PostViewset)
router.register(r'sessions', SessionViewset)
router.register(r'setups', SetupViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include('rest_framework.urls')),
    path("api/password_reset/", include('django_rest_passwordreset.urls', namespace='password_reset')),
    path("api/register/", RegisterAPI.as_view()),
    path("api/login/", LoginAPI.as_view()),
    path("api/me/", UserAPI.as_view()),
    path("api/reset/", ChangePasswordView.as_view()),
    path('api/logout/', LogoutAPI.as_view(), name='logout'),
]
