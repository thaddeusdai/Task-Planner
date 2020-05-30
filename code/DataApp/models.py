from django.db import models
from accounts.models import Account

# Create your models here.
class DataDb(models.Model):
     
# username (str), day (int), num_of_task (int)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    day = models.IntegerField()
    num_of_task = models.IntegerField(default=0)
    
    def __str__(self):
        return f'account: {self.account}| day: {self.day}| number of task(s) done: {self.num_of_task}'