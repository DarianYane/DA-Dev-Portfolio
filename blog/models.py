from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

# Post Model
class Post(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=250, null=True, blank=True)
    story = RichTextField()
    image = models.ImageField(null=True, blank=True, upload_to="Posts/images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)
    category = models.CharField(max_length=150, default = 'uncategorized')
    likes = models.ManyToManyField(User, related_name='blog_entries', blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title +" - Created by "+ str(self.author)

    def get_absolute_url(self):
        return reverse('BlogListView',)
    
    def sum_likes (self):
        return self.likes.count()

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('CreatePostView',)