from django.contrib import admin
from django.urls import path
from todo import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/tasks/', views.tasks, name="tasks"),
    path('api/tasks/<int:id>', views.task, name='task'),
    path('api/completed-tasks/', views.completedTasks, name='completed-tasks')
]
