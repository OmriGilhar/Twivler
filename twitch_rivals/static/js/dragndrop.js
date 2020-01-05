function $(id) {
  return document.getElementById(id);
}

dragula([$('drag-elements0'), $('drag-elements1'),  $('drag-elements2'),  $('drop-target')], {
  revertOnSpill: true
}).on('drop', function(el) {
  if ($('drop-target').children.length > 0) {
    $('sidebar-wrapper').innerHTML = $('drop-target').innerHTML;
  } else {
    $('sidebar-wrapper').innerHTML = "Display";
  }

});
