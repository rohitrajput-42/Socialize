from django.core import validators
from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.deletion import CASCADE
from profiles.models import Profile
from ckeditor.fields import RichTextField

class Post(models.Model):
    content = RichTextField(blank = True, null = True)
    image = models.ImageField(upload_to = 'upload/posts/', validators = [FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank = True, null = True)
    liked = models.ManyToManyField(Profile, blank = True, related_name = 'likes')
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'posts')

    def __str__(self):
        return str(self.content[:20])

    def num_likes(self):
        return self.liked.all().count()

    def num_comments(self):
        return self.comment_set.all().count()

    def main_comments(self):
        return self.comment_set.all()

    class Meta:
        ordering = ('-created',)


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.pk)

LIKE_CHOICES = {
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
}

class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    value = models.CharField(choices = LIKE_CHOICES, max_length = 10)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"