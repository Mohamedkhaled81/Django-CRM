from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Leads(models.Model):
    choices_priority = (
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),

    )
    choices_status = (
        ('new','New'),
        ('contacted','Contacted'),
        ('won','Won'),
        ('lost','Lost'),
    )

    name = models.CharField(max_length=30)
    description = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=20,choices=choices_status,default='new')
    email = models.EmailField()
    priority = models.CharField(max_length=10,choices=choices_priority)
    created_by = models.ForeignKey(User,related_name='lead',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name