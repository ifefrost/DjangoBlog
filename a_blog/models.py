from django.db import models
import uuid

# Create your models here.
class BlogPost(models.Model):
    """A blog post."""
    title = models.CharField(max_length=200)
    image = models.URLField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.title