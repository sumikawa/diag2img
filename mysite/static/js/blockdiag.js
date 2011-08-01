function genURL() {
    var diagram = $('textarea#diagram').val();
    $.post("", {diagram: diagram}, function(data) {
	var encode;
	$.each(data, function(i, d) {
            encode = d.encode;
	});
	$('img#dia').fadeOut("normal");
	history.pushState(null, "nwdiag2img", encode);
	$('img#dia').attr('src', encode + '.png').fadeIn("fast");
	// TODO: back button does not work
    });
    return false;
};

$(document).ready(function($) {
    $('textarea').autoResizeTextAreaQ({"max_rows":40});
});
