from django.contrib import admin
from .models import *
from .forms import TableCellForm


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    model = Page
    search_fields = ['name']


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    model = Header
    search_fields = ['content']


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    model = Text
    search_fields = ['content']


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    model = List
    search_fields = ['label']


class TableCellTabular(admin.TabularInline):
    model = TableCell
    extra = 0
    form = TableCellForm


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    model = Table
    inlines = [TableCellTabular]


@admin.register(TableCell)
class TableCellAdmin(admin.ModelAdmin):
    model = TableCell
    search_fields = ['content']
