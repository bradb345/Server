from django.db import models

class Project_type(models.Model):
    type = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.type}'

class Project(models.Model):
    project_name = models.CharField(max_length=25)
    Url = models.CharField(max_length=300)
    project_type = models.ManyToManyField(
        Project_type,
        related_name='project',
        blank=True
    )

    def __str__(self):
        return f'{self.project_name}'

class Comment(models.Model):
    content = models.TextField(max_length=250)
    project =  models.ForeignKey(
        Project,
        related_name='comments',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f'comment {self.id} on {self.project}'
