from django.db import models

# Create your models here.
class Alimentos(models.Model):
    nombre=models.CharField(verbose_name="Nombre del alimento", max_length=100, unique=True)
    OPCIONES_CHOICES = (
        ('opcion_1', 'Grasas'),
        ('opcion_2', 'Frutas'),
        ('opcion_3', 'Verduras'),
        ('opcion_4', 'Cereales y Legumbres'),
        ('opcion_5', 'Proteínas'),
        ('opcion_6', 'Lacteos'),
        ('opcion_7', 'Otros'),
    )
    categoria = models.CharField(max_length=50, choices=OPCIONES_CHOICES, default='opcion_7')
    calorias=models.IntegerField(verbose_name="Calorías por porción")
    hidratos=models.IntegerField(verbose_name="Hidratos de Carbono por porción")
    proteinas=models.IntegerField(verbose_name="Proteínas por porción")
    grasas=models.IntegerField(verbose_name="Grasas por porción")
    porcion=models.IntegerField(verbose_name="Tamaño de la porción", default=100)
    
    def __str__(self):
        return self.nombre +" - "+ self.categoria
    
    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimentos'