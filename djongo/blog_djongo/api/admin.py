from django.contrib import admin
from api.models import Task 
from  django.contrib.auth.models  import  Group  # new

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'created', 'image_tag']
    list_filter = ['created']
    search_fields = ('title',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["title"].label = "Title (Blogs only!):"
        return form

admin.site.register(Task, TaskAdmin)
admin.site.site_header  =  "Custom Task admin" 
admin.site.unregister(Group)