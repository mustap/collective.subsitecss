from zope.interface import Interface, implements, implementer
from zope.component import adapts, adapter, queryUtility
from zope import schema
from zope.schema.fieldproperty import FieldProperty
from zope.formlib.form import FormFields

from plone.app.controlpanel.form import ControlPanelForm
from Products.CMFDefault.formlib.schema import SchemaAdapterBase, ProxyFieldProperty
from Products.CMFPlone.interfaces import IPloneSiteRoot
from zope.site.hooks import getSite


from collective.subsitecss.imagewidget import ImageWidget
from collective.subsitecss import subsitecssMessageFactory as _


class ISubsiteCssSchema(Interface):

    logo = schema.Field(title=_(u'Upload logo'), 
                         description=_(u'Upload a new picture to replace the actual site logo.'),
                         required=False)

    link_color = schema.TextLine(title=_(u'Link color'), 
                             description=_('The link color in the content region. '),
                             required=False)

    background_color = schema.TextLine(title=_(u'Background color'), 
                                   description=_(u'The background color of the page. ie: #FF00FF'),
                                   required=False)
    
    global_menu_fontsize = schema.TextLine(title=_(u'Global menu font size'), 
                                           description=_(u'The font size you want for the global menu. ie: 14px'),
                                           required=False)

    global_menu_large_fontsize = schema.TextLine(title=_(u'Global menu large font size'), 
                                           description=_(u'The font size you want for the first items of the global menu. ie: 16px. This is only needed if you want a row of larger items above the normal sized ones.'),
                                           required=False)
    global_menu_large_item_count = schema.Int(title=_(u'Number of global menu large items'), 
                                              description=_(u'The number of large items to display in the global menu.'),
                                              required=False)

from persistent import Persistent
class SubsiteCssControlPanelAdapter(SchemaAdapterBase):
    """Control panel adapter
    """
    adapts(IPloneSiteRoot)
    implements(ISubsiteCssSchema)

    def get_logo(self): 
        return getattr(getSite(), 'logo', None)

    def set_logo(self, value):
        setattr(getSite(), 'logo', value)
    
    logo = property(get_logo, set_logo)

    link_color = ProxyFieldProperty(ISubsiteCssSchema['link_color'])
    background_color = ProxyFieldProperty(ISubsiteCssSchema['background_color'])
    global_menu_fontsize = ProxyFieldProperty(ISubsiteCssSchema['global_menu_fontsize'])
    global_menu_large_fontsize = ProxyFieldProperty(ISubsiteCssSchema['global_menu_large_fontsize'])
    global_menu_large_item_count = ProxyFieldProperty(ISubsiteCssSchema['global_menu_large_item_count'])
        

class SubsiteCssControlPanel(ControlPanelForm):

    form_fields = FormFields(ISubsiteCssSchema)
    form_fields['logo'].custom_widget = ImageWidget

    label = _('CSS settings')
    description = _('Css settings for this subsite.')
    form_name = _('CSS settings')
