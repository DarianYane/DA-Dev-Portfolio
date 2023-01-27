from django.db import models


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
    
# Create your models here.
# Student Model
class Student(models.Model):
    name = models.CharField(max_length=150, unique = True)
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

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

""" class EvaluationCriteria(models.Model):
    course_name
    commission_number
    Criteria_1
    Criteria_2
    Criteria_3
    Criteria_4
    Criteria_5
    Criteria_6
    Criteria_7
    Criteria_8
    Criteria_9
    Max_points_Criteria_1
    Max_points_Criteria_2
    Max_points_Criteria_3
    Max_points_Criteria_4
    Max_points_Criteria_5
    Max_points_Criteria_6
    Max_points_Criteria_7
    Max_points_Criteria_8
    Max_points_Criteria_9


class Delivery(models.Model):
    course_name
    commission_number
    delivery_number
    correction date """
    


