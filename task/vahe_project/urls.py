from django.urls import path
from .views import LessonListView, LessonDetailView, LessonCreateView, LessonUpdateView, LessonDeleteView

urlpatterns = [
    path('', LessonListView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('lesson/new/', LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/edit/', LessonUpdateView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),
]
