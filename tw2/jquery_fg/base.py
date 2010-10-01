
# TW2 proper imports
import tw2.core as twc
from tw2.core.resources import encoder

# tw2.jquery_core imports
from tw2.jquery_core import JQueryWidget
from tw2.jquery_core.base import jQueryJSLink
from tw2.jquery_core.base import jQueryPluginLinkMixin
from tw2.jquery_core.version import JSLinkMixin

# import from *this* package
from tw2.jquery_fg import defaults

### Links, etc...
class jQueryFGMixin(jQueryPluginLinkMixin):
    dirname = defaults._fg_dirname_
    basename='jquery-fg'
    modname = 'tw2.jquery_fg'

class jQueryFGJSLink(twc.JSLink, jQueryUIMixin):
    subdir = 'js'

class jQueryFGCSSLink(jQueryUIMixin, twc.CSSLink):
    subdir = 'css'
    extension = 'css'

### Resources
jquery_js = jQueryJSLink()
jquery_fg_css = jQueryFGCSSLink()
jquery_fg_js = jQueryFGJSLink()
