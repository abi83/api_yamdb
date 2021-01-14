from django.contrib import admin
from django import forms

from users_api.models import YamdbUser


class YamdbUserForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = YamdbUser
        fields = '__all__'


@admin.register(YamdbUser)
class YamdbUserAdmin(admin.ModelAdmin):
    can_delete = False
    form = YamdbUserForm

