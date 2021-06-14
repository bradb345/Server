from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Project, Comment, ProjectType

User = get_user_model()


class ProjectTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectType
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'profile_image')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

class PopulatedCommentSerializer(CommentSerializer):
    owner = UserSerializer()

class PopulatedProjectSerializer(ProjectSerializer):
    comments = CommentSerializer(many=True)
    # favorited_by = UserSerializer(many=True)
    project_type = ProjectTypeSerializer(many=True)
    owner = UserSerializer()
