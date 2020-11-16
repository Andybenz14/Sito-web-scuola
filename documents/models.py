from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    name = models.CharField(max_length=100, unique=True, editable=False)
    created_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.name = self.file.name
        super(Document, self).save()

    class Meta:
        ordering = ['-created_on']

    objects = models.Manager()

    def __str__(self):
        return self.file.name

