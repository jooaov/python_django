from django.contrib import admin
from .models import Question,Choice

# Register your models here.

#add modelo question ao admin DB
admin.site.register(Question)
admin.site.register(Choice)