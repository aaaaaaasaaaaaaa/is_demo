from django import forms



class SelectForm(forms.Form):
    category = forms.ChoiceField(label='Выберите категорию',
                                 choices=(('lead', 'Лиды'),
                                          ('company', 'Компании'),
                                          ('contact', 'Контакты'),
                                          ('deal', 'Сделки')),
                                 required=True)


