from django.contrib import admin
from .models import Comments
from .models import Replies


# Register your models here.
admin.site.register(Comments)
admin.site.register(Replies)