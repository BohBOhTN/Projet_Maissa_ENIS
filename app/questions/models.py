from django.db import models

class Question(models.Model):
    text = models.TextField()  # Store the question text
    category = models.CharField(max_length=100)  # Category for the question (e.g., student, employee, etc.)
    
    # Response choices
    JAMAIS = 0
    PARFOIS = 1
    SOUVENT = 2
    TOUJOURS = 3

    RESPONSE_CHOICES = [
        (JAMAIS, 'JAMAIS'),
        (PARFOIS, 'PARFOIS'),
        (SOUVENT, 'SOUVENT'),
        (TOUJOURS, 'TOUJOURS'),
    ]
    
    response_jamais = models.IntegerField(choices=RESPONSE_CHOICES, default=JAMAIS)
    response_parfois = models.IntegerField(choices=RESPONSE_CHOICES, default=PARFOIS)
    response_souvent = models.IntegerField(choices=RESPONSE_CHOICES, default=SOUVENT)
    response_toujours = models.IntegerField(choices=RESPONSE_CHOICES, default=TOUJOURS)

    def __str__(self):
        return self.text
