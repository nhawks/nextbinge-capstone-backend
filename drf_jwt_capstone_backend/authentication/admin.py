from django.contrib import admin
from .models import User
from .models import WatchList
from .models import WatchedShows


# Register your models here.
admin.site.register(User)
admin.site.register(WatchedShows)
admin.site.register(WatchList)