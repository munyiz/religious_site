from django.contrib import admin
from .models import BibleBook, BibleChapter, BibleVerse, Story, Question


admin.site.register(BibleBook)
admin.site.register(BibleChapter)
admin.site.register(BibleVerse)


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'private')
    filter_horizontal = ('authorized_users',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'private')
    filter_horizontal = ('authorized_users',)

admin.site.register(Story, StoryAdmin)
admin.site.register(Question, QuestionAdmin)

