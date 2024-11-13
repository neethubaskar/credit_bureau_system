from django.contrib import admin
from .models import Question, UserResponse

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'created_at')
    search_fields = ('question_text',)
    readonly_fields = ('created_at', 'modified_at', 'created_by', 'modified_by')

    def save_model(self, request, obj, form, change):
        """
        Automatically sets created_by and modified_by fields 
        to the current user in the admin interface.
        """
        if not obj.pk:
            obj.created_by = request.user
        obj.modified_by = request.user
        super().save_model(request, obj, form, change)

class UserResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'question__question_text')
    readonly_fields = ('created_at', 'modified_at', 'created_by', 'modified_by')

    def save_model(self, request, obj, form, change):
        """
        Automatically sets created_by and modified_by fields to 
        the current user in the admin interface.
        """
        if not obj.pk:
            obj.created_by = request.user
        obj.modified_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Question, QuestionAdmin)
admin.site.register(UserResponse, UserResponseAdmin)
