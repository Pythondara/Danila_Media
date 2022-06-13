from django.db import models


class Main_page(models.Model):  # Будущая инфа из бд
    # verbose_name='Хуй' локализирует информацию из бд на русский
    # title = models.CharField(max_length=150)
    # content = models.TextField(blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # photo = models.ImageField(upload_to='photos/%Y/%m/%d', max_lenght = 150, blank=True)
    # is_published = models.BooleanField(default=True)
    # category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True) С ковыычками если категория обьявлена позже и без, если наоборот
    # on_delete=PROTECT если мы удалим категорию, входящая в эту категорию информация не удалится\
    # null=True нужен для того,чтобы мы могли в бд оставлять это поле пустым
    pass

    # def __str__(self):
    #     return self.title

    # class Meta:                    для админки название заголовка
    #     verbose_name = ''          в единственном числе
    #     verbose_name_plural = ''   во множественном числе
    #     ordering = ['']                сортировка, если нужна


# class Category(models.Model):   Создание категорий
#     title = models.Charfield(max_lenght=150, db_index=True, verbose_name='Наименование категории ')

    # def __str__(self):
    #     return self.title

#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#         ordering = ['-title']

