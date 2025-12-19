from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, help_text="Versão do nome amigável para URLs")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

class Course(models.Model):
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='courses_taught',
        limit_choices_to={'is_instructor': True}
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cover_image = models.ImageField(upload_to='course_covers/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="Pode ser texto, markdown ou link para vídeo.")
    order = models.PositiveIntegerField(help_text="Ordem da aula no curso")

    def __str__(self):
        return f"{self.course.title} - {self.order}. {self.title}"

    class Meta:
        ordering = ['course', 'order']
        unique_together = ('course', 'order')

class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"

    class Meta:
        unique_together = ('student', 'course') # Garante que um aluno não se matricule duas vezes no mesmo curso
