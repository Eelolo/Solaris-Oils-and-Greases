from django import forms
from .models import TableCell


class TableCellForm(forms.ModelForm):
    class Meta:
        model = TableCell
        fields = ('content', 'row', 'column', 'row_span', 'col_span', 'spanned', 'thead')
        widgets = {
            'content': forms.Textarea(attrs={'rows': 1}),
        }
