from django.contrib import admin
from accounts.models import Account
from TodoApp.models import TodoDb
from DataApp.models import DataDb

# Register your models here.

admin.site.register(Account)
admin.site.register(TodoDb)
admin.site.register(DataDb)


