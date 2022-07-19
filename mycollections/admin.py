from django.contrib import admin
from .models import *


class CollectionTitleInline(admin.StackedInline):
        model = CollectionTitle
        extra = 0


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    inlines = [CollectionTitleInline,]




