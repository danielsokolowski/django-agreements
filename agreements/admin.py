from .models import *
from django.conf.urls.defaults import url, patterns
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect

class AcceptanceInline(admin.TabularInline):
    model = Acceptance
    extra = 1
    
class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 1

class AgreementAdmin(admin.ModelAdmin):
    """ Admin settings for Agreement model """
   
    ### Django admin methods
    #n/a
        
    ### list_display callables
    # generates html site url link
    def site_url(obj):
        try:
            return "<a href='%s'>%s</a>" % (obj.get_absolute_url(), obj.get_absolute_url()) 
        except (AttributeError, NoReverseMatch):
            return "N/A" # no model get_absolute_url defined or url reverse fails
    site_url.allow_tags = True
    
    ### model admin options
    save_on_top = True
    # list display reasoning: 
    # 1. click-able fields to either edit or view on site or whatever
    # 2. Then uniqely identifaible fields, identiy fields can be cickable 
    # 3. then from broad to narrow rendering/system logic
    # 4. Editable fields should be limited but no special ordering
    list_display = ['id', site_url, 'name', 'date_start', 'date_end', 'status']
    list_display_links = ['id'] # other columns from list_display to turn into edits link; defaults to first column
    #list_editable = ['status'] # from list_display but can not use fields from list_display_links
    list_filter = ['status'] # from least specific to most specific
    inlines = [AttachmentInline, AcceptanceInline]
    
   
admin.site.register(Agreement , AgreementAdmin)
