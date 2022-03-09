from rest_framework.routers import SimpleRouter
from product import views

router = SimpleRouter()


router.register(r'category', views.CategoryView)
router.register(r'view', views.ProductView)

urlpatterns = router.urls