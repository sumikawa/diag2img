function genURL() {
    var diagram = $('textarea#diagram').val();
    $.post("", {diagram: diagram}, function(data) {
	var encode;
	$.each(data, function(i, d) {
            encode = d.encode;
	});
	$('img#dia').fadeOut("fast");
	history.pushState(null, "", encode);
	// TODO: back button does not work
	$('#message').empty().prepend('Loading Image...</br>');
	$('img#dia').load(
	    function() { $('#message').empty(); }
	).attr('src', encode + '.png').fadeIn("fast");
    });
    return false;
};

$(document).ready(function($) {
    $('textarea').autoResizeTextAreaQ({"max_rows":20});
});
