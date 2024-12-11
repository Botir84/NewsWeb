from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='articles/')
    category = models.CharField(max_length=50, choices=[
        ('World', 'World'),
        ('Sports', 'Sports'),
        ('Technology', 'Technology'),
        ('Entertainment', 'Entertainment'),
    ])
    
    def __str__(self):
        return self.title