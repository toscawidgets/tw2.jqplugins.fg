
# tw2-proper imports
import tw2.core as twc
from tw2.core.resources import encoder

# imports from this package
from tw2.jquery_ui import base as uibase
from tw2.jquery_fg import base as fgbase

class MenuWidget(uibase.JQueryUIWidget):
    """
    Configurable options - Default values are next to each option:
        content: null - the menu content. It must be passed in as an option and formatted as an unordered list with anchor tags (links) for the nav options (see an example)

        width: 180 - width of menu container. Required for hierarchical menus (flyout, ipod) to calculate widths of child menus

        maxHeight: 180 - maximum height of menu (if ipod-style, height does not include breadcrumb, which can vary in height depending on content)

        positionOpts (defaults listed below) - location and orientation of the menu, relative to the button/link used to open it
            posX: 'left' - left side of the menu aligned with a side of the button, left or right

            posY: 'bottom' - top of the menu aligned with a either top or bottom of the menu

            offsetX: 0 - number of pixels to offset the menu left/right

            offsetY: 0 - number of pixels to offset the menu top/bottom

            directionH: 'right' - horizontal direction in which the menu will open, to the right or left

            directionV: 'down' - vertical direction in which the menu will open, up or down

            detectH: true - do horizontal collision detection

            detectV: true - do vertical collision detection

            linkToFront: false - set to "true," this option will create a clone of the button and place it over the menu for an overlapping visual effect

        showSpeed: 200 - speed to show/hide the menu in milliseconds

        callerOnState: 'ui-state-active' - class to change the appearance of the link/button when the menu is showing

        loadingState: 'ui-state-loading' - class added to the link/button while the menu is created

        linkHover: 'ui-state-hover' - class for menu option hover state

        linkHoverSecondary: 'li-hover' - alternate hover class, may be used for multi-level menus

    Hierarchical (iPod-style and flyout) menu defaults
        crossSpeed: 200 - transition effect speed for multi-level menus
        
        crumbDefaultText: 'Choose an option:' - text that appears in the ipod-style footer before a child menu is opened
        
        backLink: true - when set to "true", this option shows a 'back' link under the menu instead of a full breadcrumb in the ipod-style menu
        
        backLinkText: 'Back' - text for the back link (i.e., could also say 'previous')
        
        flyOut: false - multi-level menus are ipod-style by default; set this option to "true" to override and make flyout the default instead
        
        flyOutOnState: 'ui-state-default' - class added to an option when its child menu is showing
        
        nextMenuLink: 'ui-icon-triangle-1-e' - class to style the link (specifically, a span within the link) used in the multi-level menu to show the next level
        
        topLinkText: 'All' - text for the first breadcrumb that navigates back to the start of the ipod-style menu
        
        nextCrumbLink: 'ui-icon-carat-1-e' - class for setting the background image that follows each breadcrumb link (currently a carat)
    """
    resources = [
        fgbase.jquery_js,
        uibase.jquery_ui_js,
        uibase.jquery_ui_css,
        fgbase.jquery_fg_js,
        fgbase.jquery_fg_js,
    ]


    template = "tw2.jquery_fg.templates.menu"
    jqmethod = 'menu'

    items = twc.Param('A recursive dictionary of menu entries', default=[])
    label = twc.Param('A label for the menu', default='The Foo Menu')


