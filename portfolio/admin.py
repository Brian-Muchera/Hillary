from django.contrib import admin
from .models import Profile,Blog,Inquiry

admin.site.site_header='Muchera-Brian Admin'
admin.site.site_title='Muchera-Brian Admin Dashboard'

# Register your models here.
admin.site.register(Blog)
admin.site.register(Profile)
admin.site.register(Inquiry)