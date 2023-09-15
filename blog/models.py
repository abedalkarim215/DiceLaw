from django.db import models
from django.contrib.auth.models import User

# Model for blog posts
class Blog(models.Model):
    title = models.CharField(max_length=100)  # Title of the blog post
    short_description = models.CharField(max_length=200)  # Brief description of the blog post
    body = models.TextField()  # The main content of the blog post
    image = models.ImageField(upload_to='blog_images/')  # Image associated with the blog post
    tags = models.ManyToManyField('Tag')  # Tags related to the blog post
    categories = models.ManyToManyField('web.PracticeArea')  # Categories related to the blog post
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)  # Author of the blog post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the blog post was created


# Model for comments on blog posts
class Comment(models.Model):
    commenter = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='comments')  # User who commented
    comment = models.TextField()  # The content of the comment
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    # Reference to parent comment if this is a reply, else null
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the comment was created


# Model for tags
class Tag(models.Model):
    name = models.CharField(max_length=50)  # Name of the tag
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the tag was created
