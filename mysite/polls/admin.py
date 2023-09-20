# Register your models here.
from django.contrib import admin
from .models import Question, Choice, user_info, analytics,resources,education,experience,licenses_and_certifications,skills,languages,people_also_viewed,people_you_may_know,you_might_like
# admin.site.register(Question)
admin.site.register(Choice)
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"]
# admin.site.register(Question, QuestionAdmin)

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {"fields": ["question_text"]}),
#         ("Date information", {"fields": ["pub_date"]}),
#     ]
# admin.site.register(Question, QuestionAdmin)
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):

    model = Choice
    extra = 3


# class QuestionAdmin(admin.ModelAdmin):

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "was_published_recently"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)

class user_infoAdmin(admin.ModelAdmin):
    pass
admin.site.register(user_info, user_infoAdmin)

class analyticsAdmin(admin.ModelAdmin):
    pass
admin.site.register(analytics, analyticsAdmin)

class resourcesAdmin(admin.ModelAdmin):
    pass
admin.site.register(resources, resourcesAdmin)

class educationAdmin(admin.ModelAdmin):
    pass
admin.site.register(education, educationAdmin)

class experienceAdmin(admin.ModelAdmin):
    pass
admin.site.register(experience, experienceAdmin)

class licenses_and_certificationsAdmin(admin.ModelAdmin):
    pass
admin.site.register(licenses_and_certifications, licenses_and_certificationsAdmin)

class skillsAdmin(admin.ModelAdmin):
    pass
admin.site.register(skills, skillsAdmin)

class languagesAdmin(admin.ModelAdmin):
    pass
admin.site.register(languages, languagesAdmin)

class people_also_viewedAdmin(admin.ModelAdmin):
    pass
admin.site.register(people_also_viewed, people_also_viewedAdmin)

class people_you_may_knowAdmin(admin.ModelAdmin):
    pass
admin.site.register(people_you_may_know, people_you_may_knowAdmin)

class you_might_likeAdmin(admin.ModelAdmin):
    pass
admin.site.register(you_might_like, you_might_likeAdmin)