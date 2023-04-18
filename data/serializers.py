from rest_framework import exceptions, serializers, status, generics
from .models import *





class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = "__all__"




class WorkCategorySerializer(serializers.ModelSerializer):
    types = WorkTypeSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = WorkCategory
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
