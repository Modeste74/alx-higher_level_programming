$(document).ready(function () {
  $.get('https://fourtonfish.com/helloslaut/?lang=fr', function (data) {
    $('#head').text(data.hello);
  });
});
