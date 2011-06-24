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
