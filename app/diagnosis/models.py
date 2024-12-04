from django.db import models

class Diagnosis(models.Model):
    score_min = models.IntegerField()
    score_max = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return f"Score {self.score_min} - {self.score_max}: {self.message}"
