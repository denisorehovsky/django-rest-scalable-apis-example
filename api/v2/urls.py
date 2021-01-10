from rest_framework.routers import DefaultRouter

from api.v2.views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router_urlpatterns = router.urls

app_name = 'v2'
urlpatterns = router.urls
