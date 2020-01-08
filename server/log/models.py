from django.db import models

# Create your models here.

class Log(models.Model):
      title = models.CharField(max_length=120)
      dateAndTime = models.DateTimeField(auto_now=False, auto_now_add=False)

      def _str_(self):
        return self.title