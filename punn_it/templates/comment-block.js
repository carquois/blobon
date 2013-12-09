<script>
  var i = 0;
  $(".comment-block").mouseover(function() {
    $(this).find("#action-block").show();
  }).mouseout(function(){
    $(this).find("#action-block").hide();
  });

  var n = 0;
  $("div.enterleave").mouseenter(function() {
    n += 1;
    $(this).find("span").text( "mouse enter x " + n );
  }).mouseleave(function() {
    $(this).find("span").text("mouse leave");
  });

</script>
