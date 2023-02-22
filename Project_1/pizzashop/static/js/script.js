// script.js

// When the page is loaded
$(document).ready(function() {
    // Hide the order form
    $("#order-form").hide();
  
    // When the "Create pizza" button is clicked
    $("#create-pizza-btn").click(function() {
      // Hide the homepage
      $("#home-page").hide();
  
      // Show the order form
      $("#order-form").show();
    });
  });
  