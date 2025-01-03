from django.db import models

class ElektronXizmat(models.Model):
    """Elektron xizmatlar modeli."""
    nom = models.CharField(max_length=255)
    tavsif = models.TextField()
    narx = models.DecimalField(max_digits=10, decimal_places=2)
    rasm = models.ImageField(upload_to='xizmatlar/')
    kategoriya = models.ForeignKey('Kategoriya', on_delete=models.CASCADE, related_name='xizmatlar')

    def __str__(self):
        return self.nom

class Kategoriya(models.Model):
    """Kategoriya modeli."""
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
