from django.db import models

# Create your models here.
class Alimentos(models.Model):
    nombre=models.CharField(verbose_name="Nombre del alimento", max_length=100, unique=True)
    CATEGORIA_CHOICES = (
        ('Grasas', 'Grasas'),
        ('Frutas', 'Frutas'),
        ('Verduras', 'Verduras'),
        ('Cereales_Legumbres', 'Cereales y Legumbres'),
        ('Proteínas', 'Proteínas'),
        ('Lacteos', 'Lacteos'),
        ('Otros', 'Otros'),
    )
    categoria = models.CharField(verbose_name="Tipo de alimento", max_length=50, choices=CATEGORIA_CHOICES, default='Otros')
    COMIDA_CHOICES = (
        ('Desayuno', 'Desayuno'),
        ('Almuerzo', 'Almuerzo'),
        ('Merienda', 'Merienda'),
        ('Cena', 'Cena'),
    )
    comida = models.CharField(verbose_name="Comida en la que se suele consumir", max_length=150, choices=COMIDA_CHOICES, default='Almuerzo')
    calorias=models.IntegerField(verbose_name="Calorías por porción")
    hidratos=models.IntegerField(verbose_name="Hidratos de Carbono por porción")
    proteinas=models.IntegerField(verbose_name="Proteínas por porción")
    grasas=models.IntegerField(verbose_name="Grasas por porción")
    porcion=models.IntegerField(verbose_name="Tamaño de la porción", default=100)
    
    def __str__(self):
        return self.nombre +" - "+ self.comida +" - "+ self.categoria
    
    class Meta:
        verbose_name = 'Alimento'
        verbose_name_plural = 'Alimentos'