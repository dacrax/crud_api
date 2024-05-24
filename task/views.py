from rest_framework import viewsets
from .serializer import taskSerializer
from .models import task

# Create your views here.

class taskView(viewsets.ModelViewSet):
    serializer_class=taskSerializer
    queryset=task.objects.all()
