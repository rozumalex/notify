(function($) {
$(function() {
  
  $('nav.tabs-nav').on('click', 'a:not(.active)', function() {
    $(this)
      .addClass('active').siblings().removeClass('active')
      .closest('div.tabs').find('div.tab').removeClass('active').eq($(this).index()).addClass('active');
  });
  

  $("#logout-btn").click(function() {
    $("#logout-popup").fadeIn(300);  
  });
  $("#new-task-btn").click(function() {
    $("#new-task-popup").fadeIn(300);  
  });
  $(".cancel-btn").click(function() {
    $(".popup").fadeOut(300);
  });
  $(document).keyup(function(e) {
   if (e.key === "Escape") {
      $(".popup").fadeOut(300);
  }
  });
});
})(jQuery);