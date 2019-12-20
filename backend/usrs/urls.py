from rest_framework import routers
from .api import UsrViewSet

router = routers.DefaultRouter()
router.register('api/usrs',UsrViewSet, 'usrs')

urlpatterns = router.urls
