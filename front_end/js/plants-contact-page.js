// Page Animations
window.addEventListener("beforeunload", function () {
    document.body.classList.add("animate-out");
  });

// Navigation bar 
function responsiveNavbar() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

// HTTP Get request
function httpGet(theUrl) {
  let xmlHttpReq = new XMLHttpRequest();
  xmlHttpReq.open("GET", theUrl, false);
  xmlHttpReq.setRequestHeader('Content-type', 'application/json') 
  xmlHttpReq.send(null);
  return xmlHttpReq.responseText;
}

// displays basket quantities in basket icon
function displayBasketQuantity() {
  basketQuantity = httpGet(`http://127.0.0.1:5000/basket_table_data/all_items_quantity`)
  document.getElementById('lblCartCount').innerHTML = basketQuantity;
}

displayBasketQuantity();