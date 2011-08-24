<%namespace name="tw" module="tw2.core.mako_util"/>
<div id="${w.attrs['id']}:wrapper">
${w.child.display()}
<div id="${w.attrs['id']}:target" class='hidden'>
    <ul>
	% for entry in w.items:
		<%include file="recursive_menu.mak" args="item=entry" />
	% endfor
    </ul>
</div>

<script type="text/javascript">
$(function() {
    $(document).ready( function () {
        var opts = ${w.options};
        opts['content'] = $('#${w.selector}\\:target').html();
        $("#${w.selector}").${w.jqmethod}(opts);
		% if 'click' in w.events:
        $("#${w.selector}").click(${w.events['click']});
		% endif
    });
});
</script>
</div>
