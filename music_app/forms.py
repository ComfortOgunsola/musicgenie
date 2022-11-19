from django.forms import ModelForm

from .models import Artist, Song
from crispy_forms.helper import FormHelper 

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = "__all__"
        
        def __int__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
            
class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = "__all__"
    
    def __init__(self,  *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
            self.helper.render_required_fields = False 