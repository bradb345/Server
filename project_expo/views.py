# from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from .models import Project, Comment
from .serializers import ProjectSerializer, PopulatedProjectSerializer, CommentSerializer

class ProjectListView(APIView):

    def get(self, _request):
        project = Project.objects.all()
        serialized_project = PopulatedProjectSerializer(project, many=True)
        return Response(serialized_project.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['owner'] = request.user.id
        new_project = ProjectSerializer(data=request.data)
        if new_project.is_valid():
            new_project.save()
            return Response(new_project.data, status=status.HTTP_201_CREATED)
        return Response(new_project.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)    

class ProjectDetailView(APIView):

    def get_artist(self, pk):
        try :
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise NotFound()   

    def get(self, _request, pk):
        try :
            project = Project.objects.get(pk=pk) # get a artist by id (pk means primary key)
            serialized_project = PopulatedProjectSerializer(project)
            return Response(serialized_project.data,status=status.HTTP_200_OK) # send the JSON to the client 
        except Project.DoesNotExist:
            raise NotFound()  

class CommentListView(APIView):

        permission_classes = (IsAuthenticated, )

        def post(self, request, project_pk):
            request.data['project'] = project_pk
            request.data['owner'] = request.user.id
            serialized_comment = CommentSerializer(data=request.data)
            if serialized_comment.is_valid():
                serialized_comment.save()
                return Response(serialized_comment.data, status=status.HTTP_201_CREATED)
            return Response(serialized_comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)    