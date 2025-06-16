from django.db import models

class BaseModel(models.Model):
    create_at = models.DateField(auto_now_add= True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class MediaFile(BaseModel):
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.file.name