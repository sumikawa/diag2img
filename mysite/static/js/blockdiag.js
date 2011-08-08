function genURL() {
    var diagram = $('textarea#diagram').val();
    $.post("", {diagram: diagram}, function(data) {
	var encode;
	$.each(data, function(i, d) {
            encode = d.encode;
	});
	$('img#dia').fadeOut("normal");
	$('#message').prepend('Loading Image...');
	history.pushState(null, "", encode);
	// TODO: back button does not work
	$('img#dia').attr('src', encode + '.png').load(
	    function() { $('#message').empty(); }
	).fadeIn("fast");
    });
    return false;
};

$(document).ready(function($) {
    $('textarea').autoResizeTextAreaQ({"max_rows":20});
});
