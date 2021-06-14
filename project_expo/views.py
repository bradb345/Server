# from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import Project
from .serializers import ProjectSerializer

class ProjectListView(APIView):

    def get(self, _request):
        project = Project.objects.all()
        serialized_project = ProjectSerializer(project, many=True)
        return Response(serialized_project.data, status=status.HTTP_200_OK)

class ProjectDetailView(APIView):

    def get_artist(self, pk):
        try :
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise NotFound()   

    def get(self, _request, pk):
        try :
            project = Project.objects.get(pk=pk) # get a artist by id (pk means primary key)
            serialized_project = ProjectSerializer(project)
            return Response(serialized_project.data,status=status.HTTP_200_OK) # send the JSON to the client 
        except Project.DoesNotExist:
            raise NotFound()