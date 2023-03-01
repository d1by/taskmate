from django.contrib import admin

# Register your models here.

from .models import Task, Topic, Message

admin.site.register(Task)
admin.site.register(Topic)
admin.site.register(Message)