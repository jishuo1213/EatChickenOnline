from django.db import models


class DoubleColorBallHistory (models.Model):
    issue_date = models.CharField(max_length=10)
    open_code = models.CharField(max_length=20)
    open_time = models.DateTimeField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    