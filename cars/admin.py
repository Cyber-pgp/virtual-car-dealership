from django.contrib import admin
from cars.models import Car, Profile

class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'year', 'added_by']
    search_fields = ['make', 'model', 'year', 'added_by__username']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_type']
    search_fields = ['user__username', 'user_type']

admin.site.register(Car, CarAdmin)
admin.site.register(Profile, ProfileAdmin)
