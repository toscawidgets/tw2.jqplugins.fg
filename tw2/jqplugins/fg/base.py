
# TW2 proper imports
import tw2.core as twc
from tw2.core.resources import encoder

# tw2.jquery core imports
from tw2.jquery.base import jQueryJSLink, jQueryPluginLinkMixin
from tw2.jquery.version import JSLinkMixin

# import from *this* package
from tw2.jqplugins.fg import defaults

### Links, etc...
class jQueryFGMixin(jQueryPluginLinkMixin):
    dirname = defaults._fg_dirname_
    basename='fg.menu'
    modname = 'tw2.jqplugins.fg'

class jQueryFGJSLink(twc.JSLink, jQueryFGMixin):
    subdir = 'js'

class jQueryFGCSSLink(jQueryFGMixin, twc.CSSLink):
    subdir = 'css'
    extension = 'css'

### Resources
jquery_js = jQueryJSLink()
jquery_fg_css = jQueryFGCSSLink()
jquery_fg_js = jQueryFGJSLink()
