function genURL() {
    var diagram = $('textarea#diagram').val();
    diagram = diagram.split("<").join("&lt;");
    diagram = diagram.split(">").join("&gt;");
    diagram = diagram.split("\n").join("<br>");
    $('input#jsonid').attr('value', diagram);
    $('form#json').submit();
};

function update_diagram() {
};

$(document).ready(function($){
  diagram = $('#diagram');
  diagram.timer = null;

  diagram.bind('keyup change', function(){
    if (diagram.timer) clearTimeout(diagram.timer);
    diagram.timer = setTimeout(update_diagram, 500);
  });
  update_diagram();
});
