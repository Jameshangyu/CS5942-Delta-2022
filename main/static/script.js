/* Dependent forms code --jQuery*/
$(document).ready(function() {
    $('#listing').change(function() {
      $(".number1").toggle($(this).val() == '1');
    }).trigger('change.number1');
  });

$(document).ready(function() {
    $('#listing').change(function() {
      $(".number2").toggle($(this).val() == '2');
    }).trigger('change.number2');
  });

$(document).ready(function() {
    $('#listing').change(function() {
      $(".number3").toggle($(this).val() == '3');
    }).trigger('change.number3');
  });

$(document).ready(function() {
    $('#listing').change(function() {
      $(".number4").toggle($(this).val() == '4');
    }).trigger('change.number4');
  });

$(document).ready(function() {
    $('#listing').change(function() {
      $(".number5").toggle($(this).val() == '5');
    }).trigger('change.number5');
  });
