from zope.interface import Interface
from zope.component import queryUtility
from zope.site.hooks import getSite
from Products.Five import BrowserView
from Products.CMFPlone.utils import getToolByName
from Acquisition import aq_inner
from zope.component import getMultiAdapter

from collective.subsitecss.configlet import ISubsiteCssSchema

class ISubSiteCssView(Interface):
    
    def logo_tag():
        """logo tag"""

    def logo_data(self):
        """logo data"""

class SubSiteCssView(BrowserView):
    """View for subsite css data

    """

    def logo_tag(self, thumb=False):
        """logo tag"""
        w = "465"
        h =  "53"
        img = "local-logo.png"
        tools = getMultiAdapter((getSite(), self.request), name=u'plone_tools')
        purl = tools.url()

        image = getattr(getSite(), 'logo', None)
        if image:
            w = image.width
            h = image.height
            img = purl() + "/@@subsitelogo"

        if self.request.get('thumb', None):
            w = ""
            h = 40
        return '<img src="%s" height="%s" width="%s" title="Forside" alt="Forside"/>' % (img, h, w)
    
    def logo_data(self):
        image = getattr(getSite(), 'logo', None)
        self.request.RESPONSE.setHeader('content_type', image.content_type)
        return image.data
