"""
Latte-chan TEMPLATES
"""
# Standard Library Imports
from functools import cached_property

# Proxyshop Imports
import src.text_layers as text_classes
from src.templates import NormalTemplate
from src.constants import con
from src.settings import cfg
import src.helpers as psd


class <TemplateName> (NormalTemplate):
    """
     * Notes about my template here.
     * Created by <YourName>
    """
    template_suffix = "<Suffix>"

    # OPTIONAL
    @property
    def property_name(self):
        # Overwrite a property with a new value
        return some_value

    # OPTIONAL
    @cached_property
    def cached_property_name(self):
        # Cached properties are saved to memory the first time they are accessed
        # Can improve execution time for properties like layer objects
        return psd.getLayer('Some layer name')
    
    # OPTIONAL
    def __init__ (self, layout):
        # DO STUFF
        super().__init__(layout)
    
    # OPTIONAL
    def enable_frame_layers (self):
        # DO STUFF
        super().enable_frame_layers()

    # OPTIONAL
    def basic_text_layers (self):
        # DO STUFF
        super().basic_text_layers()

    # OPTIONAL
    def rules_text_and_pt_layers (self):
        # DO STUFF
        super().rules_text_and_pt_layers()