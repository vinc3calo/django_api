from django.db import models

class Post(models.Model): # creates Post table schema for migration
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model): # creates Comment table schema for migration
    post = models.ForeignKey('Post', on_delete=models.CASCADE)  # Links to a Post
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author}'