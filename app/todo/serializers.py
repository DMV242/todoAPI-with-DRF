from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.models import ToDo

class TodoSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = ToDo
        fields = ["id","title","completed","user"]
        read_only_fields=["id","user"]

    def get_user(self,instance):
        return  UserSerializer(instance.user).data




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username","email"]







