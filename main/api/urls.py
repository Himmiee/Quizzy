from django.urls import path
from .views import CreateDetailView, RetrieveDetailView, ListDetailView, DetailView, CreateOptionView, CreateCourseView


urlpatterns = [
    path("create/",CreateDetailView.as_view(), name="create_detail"),
    path("get/",ListDetailView.as_view(), name="get"),
    path("retrieve/<int:id>",RetrieveDetailView.as_view(), name="retrieve_detail"),
    path("info/<int:id>",DetailView.as_view(), name="info"),
    path("createOpt/",CreateOptionView.as_view(), name="create_option"),
    path("createCourse/",CreateCourseView.as_view(), name="create_course"),
    
]