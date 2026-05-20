from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_body = models.TextField()

    def _str_(self):
        return self.blog_title

class Comment(models.Model):
    # related_name from Comment model.
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def _str_(self):
        return self.comment
