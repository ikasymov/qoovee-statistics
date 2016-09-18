from django import forms


class ReportForm(forms.Form):
    name = forms.CharField()
    number = forms.IntegerField()

# class DailyReportForm(forms.ModelForm):

#     class Meta:
#         model = ReportField
#         fields = ('calls', 'meetings', 'contracts', 'prepayment', 'standart_shop', )
