from django.contrib import admin
from interview.models import Interview
from question.admin import QuestionInline
from django import forms
from django.core.exceptions import ValidationError


class InterviewAdminForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = "__all__"

    def clean_start(self):
        if 'start' in self.changed_data and self.instance.start:
            raise ValidationError('Не возможно поменять дату начала')
        return self.cleaned_data['start']


class InterviewAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    form = InterviewAdminForm


admin.site.register(Interview, InterviewAdmin)

