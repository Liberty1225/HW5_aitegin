from django.contrib import admin
from django.urls import path, include
from myapp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('course', views.CourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student/', views.StudentCreateListView.as_view()),
    path('api/student/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view()),

    path('api/courses/', include(router.urls)),

    path('api/mentor/', views.MentorUniversalViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/mentor/<int:pk>/', views.MentorUniversalViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]