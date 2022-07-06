from django.db import models

# Create your models here.

class vlanModel(models.Model):
    vlan_id    = models.CharField(max_length=20)
    name       = models.CharField(max_length=20)
    ip         = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
