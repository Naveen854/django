from django.db import models
from uuid import uuid4

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000,null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag',blank=True)
    vote_total = models.IntegerField(default=0,null=True, blank=True)
    vote_ratio = models.IntegerField(default=0,null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    id = models.UUIDField(default = uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    UP_VOTE = 'Up Vote'
    DOWN_VOTE = 'Down Vote'
    VOTE_TYPE=[
        ('up',UP_VOTE),
        ('down',DOWN_VOTE)
    ]
    #owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name