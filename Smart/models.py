from django.db import models



class Area(models.Model):
    name = models.CharField(max_length=128)
    topic = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    slogan = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'
    
class Title(models.Model):
    
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    

    def __str__(self):
        return f'{self.name} - ({self.area})'
    

class Service(models.Model):

    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name} - {(self.title)}'
    

class Contact(models.Model):

    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name} - {self.phone}'