from django import forms
from django.contrib import admin

from users_api.models import YamdbUser


class YamdbUserForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = YamdbUser
        fields = '__all__'


@admin.register(YamdbUser)
class YamdbUserAdmin(admin.ModelAdmin):
    form = YamdbUserForm
    list_display = ('username', 'pk', 'email', 'role',)
