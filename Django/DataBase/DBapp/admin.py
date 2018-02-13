from django.contrib import admin
from DBapp.models import Prize , Stories , Trip , Userprize , Votes , Tripcomment , Storycomment
# Register your models here.
admin.site.register(Prize)
admin.site.register(Stories)
admin.site.register(Trip)
admin.site.register(Userprize)
admin.site.register(Votes)
admin.site.register(Tripcomment)
admin.site.register(Storycomment)
