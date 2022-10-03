from djongo import models
from django.utils.safestring import mark_safe

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=52)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(upload_to = 'images/', null=True)

    def  image_tag(self):
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.pic))

    image_tag.allow_tags = True     

    class  Meta:  #new
        verbose_name_plural  =  "Tasks"

    def __str__(self):
        return self.title

    def body_preview(self):
        return self.body[:50]
       