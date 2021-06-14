from django.urls import path
from .views import ProjectListView, ProjectDetailView, CommentListView

urlpatterns = [
    path('', ProjectListView.as_view()),
    path('<int:pk>/', ProjectDetailView.as_view()),
    path('<int:project_pk>/comments/', CommentListView.as_view()),
]
