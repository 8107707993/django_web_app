from django.db import models


# Create your models here.
class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head1 = models.CharField(max_length=500,)
    chead1 = models.CharField(max_length=5000,)
    head2 = models.CharField(max_length=500,)
    chead2 = models.CharField(max_length=5000,)
    head3 = models.CharField(max_length=500,)
    chead3 = models.CharField(max_length=5000,)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.title
