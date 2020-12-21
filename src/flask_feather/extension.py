from flask import current_app
from jinja2 import Markup
from xml.dom import minidom
import io

from . import icons

class Feather(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app,'extensions'):
            app.extension= {}
        app.extensions['feather']=_feather
        app.context_processor(self.context_processor)
    
    @staticmethod
    def context_processor():
        return {
            'feather':current_app.extensions['feather']
        }
    def create(self, context):
        pass

class _feather(object):
    @staticmethod
    def icon(icon_name, **kwargs):
        """Attempt to render the icon icon_name with attributes as listed.

        Args:
            icon_name (string): The name of the feather icon
        """
        icon_name = icon_name.replace('-','_')
        if not icon_name:
            return ''
        doc = minidom.parseString(getattr(icons, icon_name))
        for attr, val in kwargs.items():
            attr = attr.replace('_','-')
            doc.documentElement.setAttribute(attr, str(val))
        writer = io.StringIO()
        SVGDocument(doc).writexml(writer)
        return Markup(writer.getvalue())

class SVGDocument:
    def __init__(self, doc: minidom.Document):
        self._doc = doc

    @property
    def doc(self) -> minidom.Document:
        return self._doc

    def writexml(self, writer, indent="", addindent="", newl=""):
        """Ignore the xml tag"""
        for node in self.doc.childNodes:
            node.writexml(writer, indent, addindent, newl)