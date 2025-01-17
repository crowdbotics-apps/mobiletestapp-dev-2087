from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    AsdsdsViewSet,
    CustomTextViewSet,
    HomePageViewSet,
    SomeModelViewSet,
    SSViewSet,
    TestViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("somemodel", SomeModelViewSet)
router.register("test", TestViewSet)
router.register("asdsds", AsdsdsViewSet)
router.register("ss", SSViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
