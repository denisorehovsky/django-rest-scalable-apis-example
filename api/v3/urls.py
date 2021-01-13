from rest_framework.routers import DefaultRouter

from api.v3.views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router_urlpatterns = router.urls

app_name = 'v3'
urlpatterns = router.urls
