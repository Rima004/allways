from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from apps.main.models import Places, Statistics

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Places)
class PlacesAdmin(ModelAdmin):
    list_display = ["name", "category"]
    search_fields = ["name"]
    list_filter = ["category"]
    ordering = ["name"]
    list_per_page = 25


@admin.register(Statistics)
class StatisticsAdmin(ModelAdmin):
    list_display = ["year", "number_of_people"]
    list_filter = ["year"]
    ordering = ["year"]
    list_per_page = 25
