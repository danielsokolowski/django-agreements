from django import forms
from django.template.loader import render_to_string
from django.conf import settings
from .models import *

class  AcceptanceForm(forms.ModelForm):
    # configuration
    class Meta:
        model =  Acceptance
        fields = ['confirmation'] # show these fields from model
        #exclude = ('Agreement') # exclude these fields from model
    
    #error_css_class = 'clsError' # defaults to .error class
    required_css_class = 'required'   
    
    # default model form fields over rides
    #content = forms.CharField(required=False, widget=CKEditorWidget(config_name='default'),
    #                              initial=render_to_string('app_name/model_name_lowercase_content_initial_value.inc.html',
    #                                                        {'STATIC_URL': settings.STATIC_URL}))
                                                            
   