from django.db import models

# Create your models here.
class model3d(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    model_glb = models.FileField(upload_to='glbs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Model_3Ds"
    def __str__(self):
        return f"{self.id},{self.name}, {self.model_glb}{self.uploaded_at},"