from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Game(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    paragraph =  models.TextField(_("Paragraph"))
    

    class Meta:
        verbose_name = _("Game")
        verbose_name_plural = _("Games")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Game_detail", kwargs={"pk": self.pk})
