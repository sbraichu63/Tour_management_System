from django.contrib import admin
from .models import Post, Provinces, Comment, enroll, Payment
# Register your models here.

admin.site.register(Post) 
admin.site.register(Provinces) 
admin.site.register(Comment) 
admin.site.register(enroll)
admin.site.register(Payment)