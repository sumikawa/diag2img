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
	$('img#dia')
	    .error(function() {
		$(this).hide();  
		$('#message').empty().prepend('<div style="color: red; background-color: yellow; text-align: center;">Error.  The diagram seems wrong</div>');
	    })
	    .load(function() {
		$(this).hide();  
		$('#image').append(this);  
		$(this).fadeIn(); 
	    })
	    .attr('src', encode + '.png').fadeIn("fast");
	$('#message').empty();
    });
    return false;
};

$(document).ready(function($) {
    $('textarea').autoResizeTextAreaQ({"max_rows":20});
});
