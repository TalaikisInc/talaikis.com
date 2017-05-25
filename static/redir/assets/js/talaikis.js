$(document).ready(function() {
   $(".flip").click(function() {
     $flip = $(this);
     $content = $flip.next();
     $content.slideToggle();
  });
});

//$("li").hover(function(){
    //$(this).css("background-color", "#e8edf3");
    //}, function(){
    //$(this).css("background-color",  "#22264b");
//});

//jrequires jQuery Easing plugin
$(function() {
  $('a.scroll').bind('click', function(event) {
    var $anchor = $(this);
    $('html, body').stop().animate({
      scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
      event.preventDefault();
    });
});
