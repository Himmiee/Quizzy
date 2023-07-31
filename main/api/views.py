from rest_framework.response import Response
from rest_framework import generics
from .models import Detail, Course, Option
from .serializers import DetailSerializer, CourseSerializer, OptionSerializer



class CreateDetailView(generics.CreateAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

class RetrieveDetailView(generics.RetrieveAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    lookup_field = "id"

class ListDetailView(generics.ListAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

class DetailView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    lookup_field = "id"

class CreateOptionView(generics.CreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class CreateCourseView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
