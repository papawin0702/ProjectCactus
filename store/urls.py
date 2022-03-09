from rest_framework.routers import SimpleRouter
from store import views

router = SimpleRouter()


router.register(r'view', views.StoreView)

urlpatterns = router.urls