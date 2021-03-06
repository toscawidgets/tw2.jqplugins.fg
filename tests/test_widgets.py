from webob import Request
from webob.multidict import NestedMultiDict
from tw2.core.testbase import assert_in_xml, assert_eq_xml, WidgetTest
from nose.tools import raises
from cStringIO import StringIO
from tw2.core import EmptyField, IntValidator, ValidationError
from cgi import FieldStorage
import formencode

import webob
if hasattr(webob, 'NestedMultiDict'):
    from webob import NestedMultiDict
else:
    from webob.multidict import NestedMultiDict

import tw2.jqplugins.ui
import tw2.jqplugins.fg.widgets as w

class TestMenuWidget(WidgetTest):
    widget = w.MenuWidget
    attrs = {'id' : 'foo'}
    params = {
        'child' : tw2.jqplugins.ui.ButtonWidget(id='blahah'),
        'items' : [
            {'name' : "Breaking News",
             'children' : [
                 {'name' : "Entertainment",},
                 {'name' : "Politics",},
                 {'name' : "A&E",},
                 {'name' : "Sports"},
             ]
            }]
    }
    expected = """
<div id="foo:wrapper">
<div id="blahah:wrapper">
<button id="blahah"></button>
<script type="text/javascript">
$(function() {
    $("#blahah").button({});
});
</script>
</div>
<div id="foo:target" class="hidden">
    <ul>
        <li><a href="#">Breaking News</a>
            <ul>
                <li><a href="#">Entertainment</a></li>
                <li><a href="#">Politics</a></li>
                <li><a href="#">A&amp;E</a></li>
                <li><a href="#">Sports</a></li>
            </ul>
        </li>
    </ul>
</div>
<script type="text/javascript">
$(function() {
    $(document).ready( function () {
        var opts = {};
        opts['content'] = $('#foo\\\\:target').html();
        $("#foo").fgmenu(opts);
    });
});
</script>
</div>
"""
