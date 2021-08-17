from django.db import models


class Category (models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Audio (models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    audio_file = models.FileField(upload_to='Audio',
                                  null=True,
                                  blank=True,
                                  verbose_name='Аудиофайл'
                                  )
    picture = models.ImageField(upload_to='Audio',
                                null=True,
                                blank=True,
                                verbose_name='Изображение')
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 related_name='audios',
                                 null=True)

    class Meta:
        verbose_name = 'Аудио'
        verbose_name_plural = 'Аудио'

    def __str__(self):
        return self.name