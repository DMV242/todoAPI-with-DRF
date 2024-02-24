from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from todo.serializers import TodoSerializer
from core.models import ToDo




class ToDoViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    queryset = ToDo.objects.all()
    permission_classes = [IsAuthenticated]


    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Overriding the create method to add a custom message when creating an ToDo with a same title
        """
        title = request.data.get("title")
        if ToDo.objects.filter(title=title).exists():
            return Response({
                "error":"to do with this title already exits"
            },status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)









