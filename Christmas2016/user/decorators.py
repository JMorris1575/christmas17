from django.contrib.auth.decorators import login_required
from django.core.exceptions import ImproperlyConfigured
from django.utils.decorators import method_decorator
from django.views.generic import View

"""
I modified this from Django Unleashed page 492.
"""

def class_login_required(cls):
    if (not isinstance(cls, type) or not issubclass(cls, View)):
        raise ImproperlyConfigured("class_login_required must be applied to subclasses of View class.")
    decorator = method_decorator(login_required)
    cls.dispatch = decorator(cls.dispatch)
    return cls

