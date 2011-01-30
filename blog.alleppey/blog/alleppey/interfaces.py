from zope.interface import Interface

from plone.theme.interfaces import IDefaultPloneLayer
from zope import schema

class IInstantMessage(Interface):
    """Marker interface
    """

class IBiofooter(Interface):
    """Marker interface
    """
#    username = schema.ASCIILine(title=u"User name",description=u"The database user name",required=True)
#   password = schema.Password(title=u"Password",description=u"The database password",required=False)
#   database = schema.ASCIILine(title=u"Database name",description=u"The name of the database on this server", required=True)


class IInstantMessageSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 skin layer 
       for this product.
    """
