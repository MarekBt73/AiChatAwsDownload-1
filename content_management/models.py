from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DifficultyLevel(models.Model):
    level = models.CharField(max_length=100)

    def __str__(self):
        return self.level

class EducationalMaterial(models.Model):
    LESSON = 'L'
    EXERCISE = 'E'
    QUIZ = 'Q'

    MATERIAL_TYPE_CHOICES = [
        (LESSON, 'Lesson'),
        (EXERCISE, 'Exercise'),
        (QUIZ, 'Quiz'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    material_type = models.CharField(max_length=1, choices=MATERIAL_TYPE_CHOICES)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    difficulty_level = models.ForeignKey(DifficultyLevel, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    difficulty_level = models.ForeignKey(DifficultyLevel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    content = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    difficulty_level = models.ForeignKey(DifficultyLevel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Ebook(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='ebooks/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    difficulty_level = models.ForeignKey(DifficultyLevel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
