from django.db import models
#from django.contrib.db import models
from django.core.urlresolvers import reverse
from django.core.urlresolvers import NoReverseMatch
from django.utils.encoding import iri_to_uri
from django.utils.http import urlquote
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator
import uuid

class AgreementManager(models.Manager):
    """
    Additional methods / constants to Agreement's objects manager:
    
    ``AgreementManager.objects.active()`` - all active instances
    """
    ### Model (db table) wide constants - we put these and not in model definition to avoid circular imports.
    ### One can access these constants through <foo>.objects.STATUS_DISABLED or ImageManager.STATUS_DISABLED
    STATUS_DISABLED = 0
    STATUS_ENABLED = 100
    STATUS_ARCHIVED = 500
    STATUS_CHOICES = (
        (STATUS_DISABLED, "Disabled"),
        (STATUS_ENABLED, "Enabled"),
        (STATUS_ARCHIVED, "Archived"),
    )
    # we keep status and filters naming a little different as
    # it is not one-to-one mapping in all situations
    def live(self):
        """ Returns all entries accessible through front end site"""
        return self.all().filter(status=self.STATUS_ENABLED)
    def retired(self):
        """ Returns entries that are live and considered 'old' """
        return self.all().filter(status=self.STATUS_ARCHIVED)

class Agreement(models.Model):
    """
    Main entity representing Agreement object
    """
    ### model options - "anything that's not a field"
    class Meta:
        ordering = ['name']
        get_latest_by = 'order'
        #order_with_respect_to = <some FK to parent model>
        #permissions = [["can_deliver_pizzas", "Can deliver pizzas"]]
        #unique_together = [["driver", "restaurant"]]
        #verbose_name = "pizza"
        #verbose_name_plural = "stories"
    
    ### django native method
    def get_absolute_url(self):
        """ Returns the relative url mapping for the instance of this model if it exists or None otherwise"""
        return iri_to_uri(reverse('AgreementDetailView', kwargs={'slug': urlquote(self.slug)}))
    
    def __unicode__(self):
        """ Retruns a unicode representation for the instance of this model """
        return u'%s' % (self.name)
        # for INTERNAL not vistor facing one can use below
        # return u'ID%s: %s - %s - %s - %s' % (self.id, self.user, self.question, self.answer, self.get_status_display())
         
        
    ### extra model functions
    #n/a
    
    ### custom managers
    objects = AgreementManager()
    #objects = models.GeoManager() # geodjango objects manager
    
    ### model DB fields
    status = models.IntegerField(choices=AgreementManager.STATUS_CHOICES, default=AgreementManager.STATUS_ENABLED)
    name = models.CharField(help_text='Name', max_length=75)
    slug = models.SlugField(help_text='An identifier label used in URL generation and used as a unique identification reference.',
                                               unique=True, null=True, validators=[RegexValidator(r'.+')], default=lambda : uuid.uuid4())
    date_start = models.DateField()
    date_end = models.DateField() 
    description = models.TextField(help_text='Optional description', blank=True)
    content = models.TextField(help_text='Optional content', blank=True)
    
    ### GeoDjango-specific fields
    #geopoint = models.PointField()
    

class AcceptanceManager(models.Manager):
    """
    Additional methods / constants to Acceptance's objects manager:
    
    ``AcceptanceManager.objects.active()`` - all active instances
    """
    ### Model (db table) wide constants - we put these and not in model definition to avoid circular imports.
    ### One can access these constants through <foo>.objects.STATUS_DISABLED or ImageManager.STATUS_DISABLED
    STATUS_DISABLED = 0
    STATUS_ENABLED = 100
    STATUS_ARCHIVED = 500
    STATUS_CHOICES = (
        (STATUS_DISABLED, "Disabled"),
        (STATUS_ENABLED, "Enabled"),
        (STATUS_ARCHIVED, "Archived"),
    )
    # we keep status and filters naming a little different as
    # it is not one-to-one mapping in all situations
    def live(self):
        """ Returns all entries accessible through front end site"""
        return self.all().filter(status=self.STATUS_ENABLED)
    def retired(self):
        """ Returns entries that are live and considered 'old' """
        return self.all().filter(status=self.STATUS_ARCHIVED)

class Acceptance(models.Model):
    """
    Main entity representing Acceptance object
    """
    ### model options - "anything that's not a field"
    class Meta:
        unique_together = [["agreement", "confirmation"]]
    
    ### django native method
    def __unicode__(self):
        """ Retruns a unicode representation for the instance of this model """
        return u'%s - %s' % (self.agreement, self.confirmation)
        # for INTERNAL not vistor facing one can use below
        # return u'ID%s: %s - %s - %s - %s' % (self.id, self.user, self.question, self.answer, self.get_status_display())
         
        
    ### extra model functions
    #n/a
    
    ### custom managers
    objects = AcceptanceManager()
    
    ### model DB fields
    status = models.IntegerField(choices=AcceptanceManager.STATUS_CHOICES, default=AcceptanceManager.STATUS_ENABLED)
    agreement = models.ForeignKey(Agreement)
    date_created = models.DateField(auto_now_add=True)
    confirmation = models.CharField(max_length=255, help_text='To accept write: Full Legal Name* - Date of Birth* - Driver License or SIN')
    