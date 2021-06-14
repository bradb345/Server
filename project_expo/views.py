# from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Project
from .serializers import ProjectSerializer

class ProjectListView(APIView):

    def get(self, _request):
        project = Project.objects.all()
        serialized_project = ProjectSerializer(project, many=True)
        return Response(serialized_project.data, status=status.HTTP_200_OK)

    
