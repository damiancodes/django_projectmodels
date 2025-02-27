from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.CharField(max_length=200)
    email=models.EmailField(null=True,blank=True)
    number=models.CharField(max_length=200, null=True,blank=True)
    date=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    post=models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    author=models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f'comment by {self.author} on {self.post}'