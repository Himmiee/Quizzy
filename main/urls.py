from django.urls import path
from .views import CreateDetailView, ListDetailView, DetailView, CreateOptionView, CreateCourseView, UpdateCourseView,UpdateOptionView
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView

urlpatterns = [
    path("create/",CreateDetailView.as_view(), name="create_detail"),
    path("get/",ListDetailView.as_view(), name="get"),
    # path("retrieve/<int:pk>",RetrieveDetailView.as_view(), name="retrieve_detail"),
    path("info/<int:pk>",DetailView.as_view(), name="info"),
    path("updOpt/<int:pk>",UpdateOptionView.as_view(), name="info"),
    path("updCourse/<int:pk>",UpdateCourseView.as_view(), name="info"),
    path("createOpt/",CreateOptionView.as_view(), name="create_option"),
    path("createCourse/",CreateCourseView.as_view(), name="create_course"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify')
    
]