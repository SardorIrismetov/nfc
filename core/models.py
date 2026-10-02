from django.db import models

class Card(models.Model):
    slug = models.CharField(max_length=255, unique=True, verbose_name="Slug (идентификатор)")
    target_url = models.URLField(blank=True, null=True, verbose_name="Целевой URL")
    is_active = models.BooleanField(default=False, verbose_name="Активна")

    def __str__(self):
        return f"{self.slug} - {'Активна' if self.is_active else 'Неактивна'}"

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"
