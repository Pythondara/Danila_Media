from django.contrib import admin
from .models import Main_page
# from .models import Category

# class Main_pageAdmin(admin.ModelAdmin):    редактируем админку и выставляем необходимые нам поля из бд
#     list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
#     list_display_links = ('id', 'title') делает названия ссылками
#     search_fields = ('title','content') поля по которым можно искать
#     list_editable = ('is_published',) редактирование публикации прямо в админке
#     list_filter = ('is_published', 'category') фильтрация списка по категориям в админке

# admin.site.register(Main_page, Main_pageAdmin) порядок регистрации важен



# class CategoryAdmin(admin.ModelAdmin):  настройка категорий для админки
#     list_display = ('id', 'title')
#     list_display_links = ('id', 'title')
#     search_fields = ('title',)



admin.site.register(Main_page)
# admin.site.register(Category, CategoryAdmin) регистрация категорий




