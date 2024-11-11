from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    department = models.CharField(max_length=50, default='IT')
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='project_images/')
    video = models.FileField(upload_to='project_videos/', default='project_videos/default.mp4')
    student_name = models.CharField(max_length=100, default='Anonymous')
    student_github = models.URLField(max_length=200, default='')
    student_linkedin = models.URLField(max_length=200, default='')
    student_email = models.EmailField(max_length=100, default='')
    student_avatar = models.ImageField(upload_to='student_avatars/', default='student_avatars/default.png')
    enrollment_number = models.CharField(max_length=20, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title