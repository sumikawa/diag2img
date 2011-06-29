function genURL() {
    var diagram = $('textarea#diagram').val();
    diagram = diagram.split("<").join("&lt;");
    diagram = diagram.split(">").join("&gt;");
    diagram = diagram.split("\n").join("<br>");
    $('input#jsonid').attr('value', diagram);
    $('form#json').submit();
};

$(document).ready(function($){
    $('textarea').autoResizeTextAreaQ({"max_rows":40});
});
