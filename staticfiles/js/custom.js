// Banner auto‐switcher
function bannerSwitcher() {
  var next = $('.content-slider input:checked').next('input');
  if (!next.length) next = $('.content-slider input').first();
  next.prop('checked', true);
}
var bannerTimer = setInterval(bannerSwitcher, 5000);
$('.controls label').click(function() {
  clearInterval(bannerTimer);
  bannerTimer = setInterval(bannerSwitcher, 5000);
});

// WOW initialization
new WOW().init();
