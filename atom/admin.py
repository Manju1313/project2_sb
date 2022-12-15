from django.contrib import admin
from atom.models import people,marks,Blog,Author,Entry
from django.db import models
from atom. models import Topic

# Register your models here.
@admin.register(people)

class peopleAdmin(admin.ModelAdmin):
    search_fields = ['first_name']
    list_display = ('first_name', 'last_name', 'age','gender','date')
    list_filter = ['gender']
    list_per_page = 5
    empty_value_display = '-empty-'
    list_display_links = ('first_name', 'last_name')
    ordering = ['first_name']

@admin.register(marks)
class marksAdmin(admin.ModelAdmin):
    list_filter = ['first_name']
    list_per_page = 2 
    list_display = ('first_name', 'Telugu', 'English','Mathematics','Biology','Physics','Chemistry','Social')
    ordering = ['first_name']
    empty_value_display = '-empty-'

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_per_page = 2

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_per_page: 2

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_per_page: 2
    empty_value_display = '-empty-'

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_filter = ['topic_name']
    list_per_page = 2 
    ordering = ['topic_name']
    list_display = ('topic_name','date')
    search_fields = ['topic_name']
