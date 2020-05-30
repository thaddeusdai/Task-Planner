from django.db import models
from accounts.models import Account

# Create your models here.
class TodoDb(models.Model):
    
    task = models.CharField(max_length = 80)
    priority = models.IntegerField(default = 1)
    completed = models.CharField(default = "No", max_length = 3)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
  #  username = models.CharField(max_length = 1000, default="None")
    description = models.CharField(default="N/A", max_length = 1000, blank=True)
   # day = models.IntegerField(default = datetime.datetime.today().day, blank=True)
    
    
    def __str__(self):
        return f'task: {self.task}/ completed {self.completed}/username: {self.account}'