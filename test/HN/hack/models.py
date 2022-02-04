from django.db import models
from django.utils.translation import gettext_lazy
from django.contrib.postgres.fields import ArrayField


# Create your models here.
ITEM_TYPE_CHOICES = ( ('S', 'story'), ('J', 'job'), ('C', 'comment'), ('P','poll'), ('O','pollopt') )



# the managers
class JobManager(models.Manager):
    def get_queryset(self):
        return super(JobManager,self).get_queryset().filter(type='J')
    
    
class StoryManager(models.Manager):
    def get_queryset(self):
        return super(StoryManager,self).get_queryset().filter(type='S')
    
    
class CommentManager(models.Manager):
    def get_queryset(self):
        return super(CommentManager,self).get_queryset().filter(type='C')
    
    
class PollManager(models.Manager):
    def get_queryset(self):
        return super(PollManager,self).get_queryset().filter(type='P')


class POManager(models.Manager):
    def get_queryset(self):
        return super(POManager,self).get_queryset().filter(type='O')
    

                                                                                

class BaseModel(models.Model):
    by = models.CharField(max_length=150, null=True)
    descendants = models.IntegerField(null=True, blank= True)
    ids = models.IntegerField(help_text="Item's unique Id", null=True)
    score = models.IntegerField(null=True, blank=True)  
    time = models.IntegerField(null=True)
    title = models.TextField(max_length=200, null=True)
    type = models.CharField(max_length=10, choices=ITEM_TYPE_CHOICES)
    url = models.URLField(max_length=200, null=True)
    kids = ArrayField(models.IntegerField(), null=True, blank=True)
    deleted = models.BooleanField(default=False, null=True)
    dead = models.BooleanField(default=False, null=True)
    text = models.TextField(gettext_lazy('text'), max_length= 500, null=True, blank=True)
    parent = models.IntegerField(null=True, blank=True)
    
    parts = ArrayField(models.IntegerField(), null=True) # list of related pollopts in display order
    
    objects = models.Manager() # The default manager.

    # custom managers
    jobin = JobManager()
    storyin = StoryManager()
    commentin = CommentManager()
    pollin = PollManager()
    pollinopt = POManager()


    REQUIRED_FIELD = ['ids', 'type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __str__(self):
        return f'item_type : {self.type}, by : {self.by}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ('-type',)

