from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import truncatechars
from django_extensions.db.fields.json import JSONField


class RequestLog(models.Model):

    ip = models.CharField(null=True, max_length=20)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    method = models.CharField(max_length=10,null=True)
    endpoint = models.CharField(max_length=200,null=True)
    time = models.DateTimeField(null=True)
    response_time = models.IntegerField(null=True)
    status_code = models.CharField(null=True, max_length=5)
    request_body = JSONField(null=True,blank=True,default={})
    query_params = JSONField(null=True,blank=True,default={})
    response_body = JSONField(null=True,blank=True,default={})


    def __str__(self):
        return str(self.ip)