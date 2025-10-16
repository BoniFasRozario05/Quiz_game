from django.contrib import admin
from base.models import Person

admin.site.site_header = "My Sql"
admin.site.site_title = "My Sql"
admin.site.index_title = "Welcome to My Sql"
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    search_fields = ('first_name',)
    list_filter = ("first_name", "last_name")
    list_per_page = 1

admin.site.register(Person, PersonAdmin)