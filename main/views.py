from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Detail, Course, Option
from .serializers import DetailSerializer, CourseSerializer, OptionSerializer



class CreateDetailView(APIView):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
    permission_classes = (IsAdminUser,)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        data={}
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data['response'] = 'successfully created a category.'
 
        return Response(data)




# class RetrieveDetailView(APIView):
#    def get(self, request,pk):
#        instance = Detail.objects.get(id=pk)
#        serializer = DetailSerializer(instance, data=request.data)
#        if serializer.is_valid():
#         info = {
#             "data":serializer.data
#         }
#         return Response(info)


class ListDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        details = Detail.objects.all()
        serializer = DetailSerializer(details, many=True)
        info = {
            "data":serializer.data
        }
        return Response(info)
    

class DetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self, request, pk):
        try:
            instance = Detail.objects.get(id=pk)
        except Detail.DoesNotExist:
            return Response({'error': 'info not found'}, status=404)
        serializer = DetailSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors, status=400)
    
    def delete(self, request, pk):
        try:
             instance = Detail.objects.get(id=pk)
             instance.delete()
             return Response({"message": "Deleted successfully"}, status=200)
        except Detail.DoesNotExist:
             return Response({"message": "Id does not exist"}, status=400)

class CreateOptionView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request):
        details = Option.objects.all()
        serializer = OptionSerializer(details, many=True)
        info = {
            "data":serializer.data
        }
        return Response(info)   
    
class UpdateOptionView(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self, request, pk):
        try:
            instance = Option.objects.get(id=pk)
        except Option.DoesNotExist:
            return Response({'error': 'info not found'}, status=404)
        serializer = OptionSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors, status=400)
    
    def delete(self, request, pk):
        try:
             instance = Option.objects.get(id=pk)
             instance.delete()
             return Response({"message": "Deleted successfully"}, status=200)
        except Option.DoesNotExist:
             return Response({"message": "Id does not exist"}, status=400)

    

class CreateCourseView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request):
        details = Course.objects.all()
        serializer = CourseSerializer(details, many=True)
        info = {
            "data":serializer.data
        }
        return Response(info)
    

class UpdateCourseView(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self, request, pk):
        try:
            instance = Course.objects.get(id=pk)
        except Course.DoesNotExist:
            return Response({'error': 'info not found'}, status=404)
        serializer = CourseSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors, status=400)
    
    def delete(self, request, pk):
        try:
             instance = Course.objects.get(id=pk)
             instance.delete()
             return Response({"message": "Deleted successfully"}, status=200)
        except Course.DoesNotExist:
             return Response({"message": "Id does not exist"}, status=400)

    
