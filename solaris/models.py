from django.db import models
from django_jsonform.models.fields import ArrayField


class Page(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    title = models.CharField(max_length=100, blank=True, default='')

    nav_page = models.BooleanField(default=False)
    catalog_page = models.BooleanField(default=False)

    def __str__(self):
        return f"Page {self.name}"


class Header(models.Model):
    tag = models.CharField(max_length=2, blank=True, default='')
    content = models.TextField(blank=True, default='')

    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='headers')
    page_index = models.IntegerField()

    def __str__(self):
        return f"Header {self.tag} from page {self.page.name}"


class Text(models.Model):
    content = models.TextField(blank=True, default='')

    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='text')
    page_index = models.IntegerField()

    def __str__(self):
        return f"Text {self.id} from page {self.page.name}"


class List(models.Model):
    label = models.TextField(blank=True, default='')
    content = ArrayField(models.TextField(null=True, blank=True), blank=True, default=list)

    rows = models.IntegerField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='lists')
    page_index = models.IntegerField()

    def __str__(self):
        return f"List {self.id} from page {self.page.name}"


class Table(models.Model):
    rows = models.IntegerField(default=0)
    columns = models.IntegerField(default=0)

    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='tables')
    page_index = models.IntegerField()

    def __str__(self):
        return f"Table {self.id} from page {self.page.name}"


class TableCell(models.Model):
    content = models.TextField(blank=True, default='')
    row_span = models.IntegerField()
    col_span = models.IntegerField()
    spanned = models.BooleanField(default=False)
    thead = models.BooleanField(default=False)

    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='cells')
    row = models.IntegerField()
    column = models.IntegerField()

    def __str__(self):
        return f"Table Cell {self.row}-{self.column} from table {self.table.id}"

    class Meta:
        ordering = ['row', 'column']
