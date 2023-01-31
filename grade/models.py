from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

"""     title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=250, null=True, blank=True)
    story = RichTextField()
    image = models.ImageField(null=True, blank=True, upload_to="Posts/images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)
    category = models.CharField(max_length=150, default = 'uncategorized')
    likes = models.ManyToManyField(User, related_name='blog_entries', blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title +" - Created by "+ str(self.author) """

"""     def get_absolute_url(self):
        return reverse('BlogListView',)
    
    def sum_likes (self):
        return self.likes.count() """

# Category Model
""" class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name """

"""     def get_absolute_url(self):
        return reverse('CreatePostView',) """
    
"""         COMIDA_CHOICES = (
        ('Desayuno', 'Desayuno'),
        ('Almuerzo', 'Almuerzo'),
        ('Merienda', 'Merienda'),
        ('Cena', 'Cena'),
    )
    comida = models.CharField(verbose_name="Comida en la que se suele consumir", max_length=150, choices=COMIDA_CHOICES, default='Almuerzo') """
    
# Create your models here.
# Student Model
class Student(models.Model):
    name = models.CharField(max_length=150, unique = True)
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ["-id"]

    def __str__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=50, unique = True)
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.course_name

class Commission(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    commission_number = models.IntegerField(unique = True)

    class Meta:
        verbose_name = 'Commission'
        verbose_name_plural = 'Commissions'

    def __str__(self):
        return str(self.course_name) +" - "+ str(self.commission_number)

class Tasks_to_Evaluate(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Task to Evaluate'
        verbose_name_plural = 'Tasks to Evaluate'

    def __str__(self):
        return str(self.title) +" - "+ str(self.subtitle)

class Terms_of_Delivery(models.Model):
    comission = models.ForeignKey(Commission, on_delete=models.CASCADE)
    number_of_delivery = models.IntegerField(validators=[MinValueValidator(0)], default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    Criteria_01 = models.ForeignKey(Tasks_to_Evaluate, on_delete=models.CASCADE, null=True, blank=True, related_name='grade.Terms_of_Delivery.Criteria_01+')
    Max_points_Criteria_01 = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    Criteria_02 = models.ForeignKey(Tasks_to_Evaluate, on_delete=models.CASCADE, null=True, blank=True, related_name='grade.Terms_of_Delivery.Criteria_02+')
    Max_points_Criteria_02 = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    Criteria_03 = models.ForeignKey(Tasks_to_Evaluate, on_delete=models.CASCADE, null=True, blank=True, related_name='grade.Terms_of_Delivery.Criteria_03+')
    Max_points_Criteria_03 = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    Criteria_04 = models.ForeignKey(Tasks_to_Evaluate, on_delete=models.CASCADE, null=True, blank=True, related_name='grade.Terms_of_Delivery.Criteria_04+')
    Max_points_Criteria_04 = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    Criteria_05 = models.ForeignKey(Tasks_to_Evaluate, on_delete=models.CASCADE, null=True, blank=True, related_name='grade.Terms_of_Delivery.Criteria_05+')
    Max_points_Criteria_05 = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    Criteria_06 = models.ForeignKey(Tasks_to_Evaluate, on_delete=models.CASCADE, null=True, blank=True, related_name='grade.Terms_of_Delivery.Criteria_06+')
    Max_points_Criteria_06 = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    Criteria_07 = models.ForeignKey(Tasks_to_Evaluate, on_delete=models.CASCADE, null=True, blank=True, related_name='grade.Terms_of_Delivery.Criteria_07+')
    Max_points_Criteria_07 = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    Criteria_08 = models.ForeignKey(Tasks_to_Evaluate, on_delete=models.CASCADE, null=True, blank=True, related_name='grade.Terms_of_Delivery.Criteria_08+')
    Max_points_Criteria_08 = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    Criteria_09 = models.ForeignKey(Tasks_to_Evaluate, on_delete=models.CASCADE, null=True, blank=True, related_name='grade.Terms_of_Delivery.Criteria_09+')
    Max_points_Criteria_09 = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    Criteria_10 = models.ForeignKey(Tasks_to_Evaluate, on_delete=models.CASCADE, null=True, blank=True, related_name='grade.Terms_of_Delivery.Criteria_10+')
    Max_points_Criteria_10 = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        verbose_name = 'Terms of Delivery'
        verbose_name_plural = 'Terms of Delivery'
        ordering = ["-id"]

    def __str__(self):
        return "Delivery #"+ str(self.number_of_delivery) + " / " + str(self.comission) + " starting on " + str(self.start_date) + " and ending on " + str(self.end_date)


class Rating(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    terms_of_delivery = models.ForeignKey(Terms_of_Delivery, on_delete=models.CASCADE)
    URL_delivery = models.URLField(blank=True, null=True)
    correction_date = models.DateField(auto_now=False, auto_now_add=True)
    criteria_01_score = models.IntegerField(default=25, validators=[MinValueValidator(0), MaxValueValidator(100)])
    criteria_02_score = models.IntegerField(default=25, validators=[MinValueValidator(0), MaxValueValidator(100)])
    criteria_03_score = models.IntegerField(default=25, validators=[MinValueValidator(0), MaxValueValidator(100)])
    criteria_04_score = models.IntegerField(default=25, validators=[MinValueValidator(0), MaxValueValidator(100)])

    total_score = models.IntegerField(default=100, validators=[MinValueValidator(0), MaxValueValidator(100)])
    rating_choices = (
        ('Óptimo', 'Óptimo'),
        ('Correcto', 'Correcto'),
        ('Bajo', 'Bajo'),
    )
    rating = models.CharField(verbose_name="Calificación final de la entrega: >= 80es 'Óptimo', entre 51 y 79 es 'Correcto', y menos o igual a 50 es 'Bajo'", max_length=50, choices=rating_choices, default='Óptimo')
    comment = models.TextField(default="Hola ###,\nEl trabajo está perfecto.\nSólo como un detalle, te recomiendo que te acostumbres a dejar comentarios en el código explicando qué hace cada porción de código.\nFelicitaciones!")
    
    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        ordering = ["-correction_date"]

    def __str__(self):
        return "Rating to "+ str(self.student) + " on " + str(self.correction_date) + " - Final RATING: " + str(self.rating) + " (" + str(self.total_score) + ")"

