from django.contrib import admin
from .models import model3d
# Register your models here.
@admin.register(model3d)
class ModelAdmin(admin.ModelAdmin):
    list_display = ("id","name", "model_glb", "uploaded_at")
    pass