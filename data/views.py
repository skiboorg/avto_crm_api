from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class GetClients(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class GetCategories(generics.ListAPIView):
    serializer_class = WorkCategorySerializer
    queryset = WorkCategory.objects.all()


class SaveClient(APIView):
    def post(self,request):
        data = request.data
        print(data)
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response(status=200)