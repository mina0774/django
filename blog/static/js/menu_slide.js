$(function(){
	$("#grid .item .accordionTitle").click(function(){
		$("#grid ul ul").slideUp();
		if(!$(this).next().is(":visible"))
		{
			$(this).next().slideDown();
		}
	});
});
