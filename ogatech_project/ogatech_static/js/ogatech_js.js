$(function () {
  $(".hide-show").show();
  $(".hide-show span").addClass("show");

  $(".hide-show span").click(function () {
    if ($(this).hasClass("show")) {
      $(this).text("Hide");
      $('input[name="login[password]"]').attr("type", "text");
      $(this).removeClass("show");
    } else {
      $(this).text("Show");
      $('input[name="login[password]"]').attr("type", "password");
      $(this).addClass("show");
    }
  });

  $('form button[type="submit"]').on("click", function () {
    $(".hide-show span").text("Show").addClass("show");
    $(".hide-show")
      .parent()
      .find('input[name="login[password]"]')
      .attr("type", "password");
  });
});

function calculateTotal() {
  let unit_price = {
    per_weight: 5,
    home_delivery: 10,
  };
  let weight_price = {};

  weight_price.per_weight = $("#weight").val() * unit_price.per_weight;
  // $("#total_value").val(weight_price.per_weight);
  let total = weight_price.per_weight + unit_price.home_delivery;

  $("#total_value").text(total);
}

$(function () {
  $(".price-input").on("change keyup", calculateTotal);
});
