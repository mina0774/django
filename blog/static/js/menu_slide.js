$(function(){
	$("#grid .item .accordionTitle").mouseover(function(){
		$("#grid ul ul").slideUp();
		if(!$(this).next().is(":visible"))
		{
			$(this).next().slideDown();
		}
	});
});
