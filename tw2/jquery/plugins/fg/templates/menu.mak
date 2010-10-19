<%namespace name="tw" module="tw2.core.mako_util"/>
<div id="${w.attrs['id']}-wrapper">
${w.child.display()}
<div id="${w.attrs['id']}-target" class='hidden'>
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
        opts['content'] = $('#${w.attrs["id"]}-target').html();
        $("#${w.attrs['id']}").${w.jqmethod}(opts);
		% if w.click:
        $("#${w.attrs['id']}").click(${w.click});
		% endif
    });
});
</script>
</div>
