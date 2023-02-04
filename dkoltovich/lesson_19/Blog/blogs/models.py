from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=128, null=True, blank=True)

    creation_date = models.DateTimeField(auto_now=True)


class ModelChangeLogsModel(models.Model):
    user_id = models.BigIntegerField(null=False, blank=True, db_index=True)
    table_name = models.CharField(max_length=132, null=False, blank=True)
    table_row = models.BigIntegerField(null=False, blank=True)
    data = models.TextField(null=False, blank=True)
    action = models.CharField(max_length=16, null=False, blank=True)  # saved or deleted
    timestamp = models.DateTimeField(null=False, blank=True)

    class Meta:
        app_label = "blog"
        db_table = "model_change_logs"