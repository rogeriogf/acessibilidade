from django.db import models

class AcessoRFID(models.Model):
    uid = models.CharField(max_length=50)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.uid} - {self.data_hora}'