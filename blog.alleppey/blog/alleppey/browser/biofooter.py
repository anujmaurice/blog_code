"""A report of recently modified cinemas and films
"""

from DateTime import DateTime

from Acquisition import aq_inner

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName

from blog.alleppey.interfaces import IBiofooter

from plone.memoize.instance import memoize
import pdb

from zope.interface import implements
from zope.component import getMultiAdapter
from zope.viewlet.interfaces import IViewlet

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class BioFooter(BrowserView):
    """View for showing recent cinema and film modifications
    """
        
    template = ViewPageTemplateFile('biofooter.pt')
        
    def __call__(self):
        # Hide the editable-object border
        self.request.set('disable_border', True)

	if self.request.get("datafile"):
		urltool = getToolByName(self, "portal_url")
		portal  = urltool.getPortalObject()
		# if attr already exist .. in case of editing 
		if not hasattr(portal,"profile_img"):
			portal.invokeFactory("Image","profile_img")
		profile_img = getattr(portal,"profile_img")
		profile_img.setImage(self.request.get("datafile"))
                if hasattr(self.request,"description"):
                    profile_img.desc = self.request.description
                pdb.set_trace()
        return self.template()
    def have_desc(self):
        urltool = getToolByName(self, "portal_url")
        portal  = urltool.getPortalObject()
        if hasattr(portal,"profile_img"):
            if hasattr(portal.profile_img,"desc"):
                return portal.profile_img.desc
        return ":)"
class BioFooterViewlet(BrowserView):
	"""Viewlet for allowing users to rate a film
	"""
	implements(IViewlet)
	render = ViewPageTemplateFile('biofooterviewlet.pt')
	def __init__(self, context, request, view, manager):
		super(BioFooterViewlet, self).__init__(context, request)
		self.__parent__ = view
		self.view = view
		self.manager = manager
		
		self.portal_state = getMultiAdapter((context, self.request),
		name=u"plone_portal_state")
	def have_score(self):
		urltool = getToolByName(self, "portal_url")
		portal  = urltool.getPortalObject()
                return "http://localhost:8080/blog/profile_img"
        def have_desc(self):
            urltool = getToolByName(self, "portal_url")
            portal  = urltool.getPortalObject()
            if hasattr(portal,"profile_img"):
                if hasattr(portal.profile_img,"desc"):
                    return portal.profile_img.desc
            return ":)"
                
            

        
 
