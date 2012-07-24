from django.views.generic import DetailView
from agreements.models import Agreement
from .forms import *
from django.views.generic.edit import FormMixin

class AgreementDetailView(DetailView, FormMixin):
    """  
    Detail view for a Agreement instance. 
    
    The instance is retrieved using a **<pk>** or **<slug>** pattern matching as defined in app's urls.py definition.
    
    The search query set is limited to objects that are statues all but **STATUS_INACTIVE**.
    
    **Templates**
    
        :template:`agreements/agreement_detail.html`

            Detail view template for Agreement instance.
        
    **Context**
        
    Adds following variables to the template context scope:
        
        ``agreement_object`` - an instance of :model:`agreements.Agreement` matching the <pk> or <slug> using live() manager query.
        ``acceptance_form`` - a bound/unbound form instance of acceptance of aggreement

    """
    ### view's settings
    #queryset = Ad.objects.none() # default query is empty
    #context_object_name="agreement" #if not specified defaults to lower object name
    context_object_name = 'agreement_object' # this is django default and is easier for templating
    queryset = Agreement.objects.live() # calls active() method on our custom manger.
    form_class = AcceptanceForm
    
    ### view's methods overrides 
    ### view's methods overrides 
    def get_context_data(self, **kwargs):
        """ Adds extra content to our template """
        context = super(AgreementDetailView, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context['acceptance_form'] =  form
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            acceptance_new = form.save(commit=False) 
            acceptance_new.agreement = self.object
            acceptance_new.save()
            
        return self.render_to_response(context)
 