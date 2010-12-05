"""A report of recently modified cinemas and films
"""

from DateTime import DateTime

from Acquisition import aq_inner

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName

from example.archetype.interfaces import IInstantMessage

from plone.memoize.instance import memoize

from kss.core import kssaction
from plone.app.kss.plonekssview import PloneKSSView
from zope.interface import implements, alsoProvides
from plone.app.layout.globals.interfaces import IViewView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

import pdb

class ActivityReportView(BrowserView):
    """View for showing recent cinema and film modifications
    """
        
    template = ViewPageTemplateFile('activityreport.pt')
        
    def __call__(self):
        # Hide the editable-object border
        self.request.set('disable_border', True)

        return self.template()
        
    def recently_modified_blogs(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        results = []
	#pdb.set_trace()
        for r in catalog(object_provides=IInstantMessage.__identifier__,
                         modified=dict(query=self.modified_after(), range='min'),
                         sort_on='modified',
                         sort_order='reverse',):
	    #pdb.set_trace()
            results.append(dict(url=r.getURL(),
                                title=r.Title,
                                description=r.Description,
				creator =r.Creator,
				date = r.CreationDate,
                                subject  = r.Subject))
	print self.split_ofthree(results)
        return self.split_ofthree(results)

    def latest(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        results = []
	#pdb.set_trace()
        for r in catalog(object_provides=IInstantMessage.__identifier__,
                         modified=dict(query=self.modified_after(), range='min'),
                         sort_on='modified',
                         sort_order='reverse',):
	    #pdb.set_trace()
            results.append(dict(url=r.getURL(),
                                title=r.Title,
                                description=r.Description,
				creator =r.Creator,
				date = r.CreationDate,
                                subject  = r.Subject))
        return results[0]
        
    def modified_after(self):
	self.days = 70
        return DateTime() - self.days

    def split_ofthree(self,a):
	i = 0
	l = len(a)
	aa=[]
	while i < l:
		aa.append(self.dict_assign(a.__getslice__(i,i+3)))
		i = i+3
	return aa

    def dict_assign(self,ww):
	dict = {}
	try:
		dict["1"]= ww[0]
		dict["2"] = ww[1]
		dict["3"] =ww[2]
	except:
            if len(dict.keys())==2:
                dict["3"]=""
            else:
                dict["2"]=""
                dict["3"]=""
	return dict

class ActivityReportVieww(BrowserView):
    """View for showing recent cinema and film modifications
    """
        
    template = ViewPageTemplateFile('morer.pt')
        
    def __call__(self):
        # Hide the editable-object border
        self.request.set('disable_border', True)

        return self.template()
    def score(self):
        return "111"

        
 
class DynamicActivityReportView(PloneKSSView):
    """View for showing recent cinema and film modifications
    """
        
    #render = ViewPageTemplateFile('Morer.pt')

    @kssaction
    def get_More(self,count):
        print "##"*20
        xtra1 = """<div id="more">
<form action="http://localhost:8080/blog" method="get">
<!-- <span class="kssattr-count-yep">MORE</span> -->
<input type="submit" value="More" class="kssattr-count-yes submitting">
</form>
</div>"""
        pdb.set_trace()
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        results = []
        alsoProvides(self, IViewView)

        ksscore = self.getCommandSet('core')
        zopecommands = self.getCommandSet('zope')
        selector = ksscore.getHtmlIdSelector('more')
        xtra = context.unrestrictedTraverse('Morer').template()
        return ksscore.replaceHTML(selector,xtra,withKssSetup='True')
