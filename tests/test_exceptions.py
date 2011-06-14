
import tw2.core as twc
import tw2.jqplugins.fg


def request_local_tst():
    global _request_local, _request_id
#    if _request_id is None:
#        raise KeyError('must be in a request')
    if _request_local == None:
        _request_local = {}
    try:
        return _request_local[_request_id]
    except KeyError:
        rl_data = {}
        _request_local[_request_id] = rl_data
        return rl_data

twc.core.request_local = request_local_tst
_request_local = {}
_request_id = 'whatever'

def setup():
    twc.core.request_local = request_local_tst
    twc.core.request_local()['middleware'] = twc.make_middleware()

def test_exception_nochild():
    w = tw2.jqplugins.fg.MenuWidget(id='foobar')
    try:
        w.display()
        assert(False)
    except ValueError as e:
        assert(str(e) == 'MenuWidget must be supplied a child parameter')

def test_exception_weirdtype():
    w = tw2.jqplugins.fg.MenuWidget(
        id='foobar',
        child=tw2.jqplugins.ui.AccordionWidget,
    )
    try:
        w.display()
        assert(False)
    except ValueError as e:
        print str(e)
        assert(str(e)=='MenuWidget child must be of type ButtonWidget not ' +
               "<class 'tw2.core.params.AccordionWidget_s'>")


