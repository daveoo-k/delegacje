from django import forms
from .models import Wyjazd

class WyjazdSzukaj(forms.Form):
    #data_wyszukiwania = forms.DateField(help_text='yyyy-mm-dd')
    id_wyszukiwania = forms.IntegerField()
    #osoba_wyszukiwania = forms.CharField(max_length=200)
    class Meta:
        model = Wyjazd


class WyjazdFormularz(forms.Form):
    nazwa = forms.CharField(max_length=200, widget= forms.TextInput(
            attrs= {
                'placeholder':"nasz zajebisty cel",
        }
        )
    )
    data_wy     = forms.DateTimeField(help_text='YYYY-MM-DD HH:MM')
    czas_do     = forms.DecimalField (decimal_places=2,help_text=' hh,mm',max_digits=10)
    czas_po     = forms.DecimalField (decimal_places=2,help_text=' hh,mm',max_digits=10)
    data_po     = forms.DateTimeField(help_text='YYYY-MM-DD HH:MM')
    osoby       = forms.CharField(max_length=430)
    samochod    = forms.CharField (max_length=20)
    j_sniadanie  = forms.IntegerField()
    j_obiad      = forms.IntegerField()
    j_kolacja    = forms.IntegerField()


    class Meta:
        model = Wyjazd
        fields = ['nazwa','data_wy','czas_do','czas_po','data_po','osoby','samochod','jedzenie']

