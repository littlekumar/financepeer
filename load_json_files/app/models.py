from django.db import models
from django import forms
from django.forms import ClearableFileInput

# for deleting media files after record is deleted
from django.db.models.signals import post_delete
from django.dispatch import receiver


class File(models.Model):
    file        = models.FileField('Upload Files', upload_to='files_temp/')
    uploaded_on   = models.DateTimeField('Uploaded On', auto_now_add=True)

    class Meta:
        db_table = 'file_session'

class UploadFileModelForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }

# delete the resume files associated with each object or record
@receiver(post_delete, sender=File)
def submission_delete(sender, instance, **kwargs):
    instance.file.delete(False)



class Files(models.Model):
    file        = models.FileField('Upload Files', upload_to='files/')
    uploaded_on   = models.DateTimeField('Uploaded On', auto_now_add=True)

    class Meta:
        db_table = 'files'


class file_Json_data(models.Model):
    user_id = models.IntegerField()
    u_id = models.IntegerField()
    title = models.CharField(max_length=144)
    body = models.TextField()
    files_id = models.IntegerField()

    class Meta:
        db_table = 'file_j_data'

class files_data(models.Model):
    json_data = models.IntegerField()
    files = models.IntegerField()

    class Meta:
        db_table = 'files_data'