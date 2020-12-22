from flask import current_app
from jinja2 import Markup
from xml.dom import minidom
import io
import os
from os import path
import re

from . import icons

class Feather(object):
    def __init__(self, app=None, import_dir=None):
        if app is not None:
            self.init_app(app)
        if import_dir is not None:
            #print(f"Attempting to import custom svg from {import_dir}")
            files = [f for f in os.listdir(import_dir)
                 if path.isfile(path.join(import_dir, f))]
            #print(f"{len(files)} file(s) found")
            for file in files:
                #print(f"Parsing {file}")
                icon_name = str(file.split('.')[0]).replace('-', '_')
                with open(path.join(import_dir, file),'r') as icon:
                    svg = icon.read()
                svg = re.sub(r'\n', r' ', svg)
                svg = re.sub(r'\s+', r' ', svg)
                svg = svg.replace('> <', '><').replace(' />', '/>')
                setattr(icons, icon_name, svg)

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