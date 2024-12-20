from django.urls import path
from . import views
from django.contrib import admin
from.import views
from django.urls import path, re_path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
schema_view = get_schema_view(
    openapi.Info(
        title="Course Management API",
        default_version="v1",
        description="API documentation for the Course Management system.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@coursemanagement.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],

)

router = DefaultRouter()
router.register(r"user_registration",UserRegistrationView)
router.register(r"add_course",AddCourseView)
router.register(r"add_semester",AddSemesterView)
router.register(r'add_subject',AddSubjectView)
router.register(r"browse_course",BrowseCourseView,basename='browse_course')


urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),

    path("",include(router.urls)),
    # path('admin/', admin.site.urls),
    path('login/',CustomTokenObtainPairView.as_view(),name='login'),
    path('view_course/',ViewCourseView.as_view({'get':'list'}),name='view_course'),
    path('delete_course/', DeleteCourseView.as_view(), name='delete_course'),
    path('add_review/', CreateReviewView.as_view(), name='add_review'),
    path('update_course/',UpdateCourseView.as_view(),name='update_course'),
    path('update_semester/',views.UpdateSemesterView.as_view(),name='update_semester'),
    path('update_subject/',views.UpdateSubjectView.as_view(),name='update_subject'),
    path('view_review/',ViewCourseReviewView.as_view({'get':'list'}),name='view_review'),
    path('view_semester/',ViewSemesterView.as_view({'get':'list'}),name='view_semester'),
    path('view_subject/',ViewSubjectView.as_view({'get':'list'}),name='view_subject'),
    path('delete_review/',DeleteReviewView.as_view(),name='delete_review'),
    path('delete_semester/',DeleteSemesterView.as_view(),name='delete_semester'),
    path('delete_subject/',DeleteSubjectView.as_view(),name='delete_subject'),
    # path('browse_course/',views.BrowseCourseView.as_view({'get': 'list'}),name='browse_course'),
]












