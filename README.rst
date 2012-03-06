tw2.jqplugins.fg
=====================

:Author: Ralph Bean <rbean@redhat.com>

.. comment: split here

.. _toscawidgets2 (tw2): http://toscawidgets.org/documentation/tw2.core/
.. _jQuery UI: http://jqueryui.com/
.. _jQuery: http://jquery.com/
.. _filament group: http://www.filamentgroup.com/

tw2.jqplugins.fg is a `toscawidgets2 (tw2)`_ wrapper for a bunch of random widgets and tools from the awesome `filament group`_.

Live Demo
---------
Peep the `live demonstration <http://tw2-demos.threebean.org/module?module=tw2.jqplugins.fg>`_.

Links
-----
Get the `source from github <http://github.com/toscawidgets/tw2.jqplugins.fg>`_.

`PyPI page <http://pypi.python.org/pypi/tw2.jqplugins.fg>`_
and `bugs <http://github.com/toscawidgets/tw2.jqplugins.fg/issues/>`_

Description
-----------

`toscawidgets2 (tw2)`_ aims to be a practical and useful widgets framework
that helps people build interactive websites with compelling features, faster
and easier. Widgets are re-usable web components that can include a template,
server-side code and JavaScripts/CSS resources. The library aims to be:
flexible, reliable, documented, performant, and as simple as possible.

The `filament group`_ designs engaging user interfaces for web
applications, mobile devices and touchscreen kiosks that are simple
and accessible to everyone.

This module, tw2.jqplugins.fg, provides `toscawidgets2 (tw2)`_ access to random `filament group`_ widgets.

Sampling tw2.jqplugins.fg in the WidgetBrowser
----------------------------------------------

The best way to scope out ``tw2.jqplugins.fg`` is to load its widgets in the
``tw2.devtools`` WidgetBrowser.  To see the source code that configures them,
check out ``tw2.jqplugins.fg/tw2/jqplugins/fg/samples.py``

To give it a try you'll need git, python, and `virtualenvwrapper
<http://pypi.python.org/pypi/virtualenvwrapper>`_.  Run::

    $ git clone git://github.com/toscawidgets/tw2.jqplugins.fg.git
    $ cd tw2.jqplugins.fg
    $ mkvirtualenv tw2.jqplugins.fg
    (tw2.jqplugins.fg) $ pip install tw2.devtools
    (tw2.jqplugins.fg) $ python setup.py develop
    (tw2.jqplugins.fg) $ paster tw2.browser

...and browse to http://localhost:8000/ to check it out.
