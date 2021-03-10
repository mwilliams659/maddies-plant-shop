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


//  Display All Basket Table Data

function displayBasket() {
  allBasketData = httpGet(`http://127.0.0.1:5000/basket_table_data`)
  // console.log(basketData['basket_table'])
  let data = JSON.parse(allBasketData);
  // console.log(data['basket_table'][0]) - this displays the arrays in the baskettable. Uses the index to access the values.
  plantName = data['basket_table'][0][1]
  plantQuantity = data['basket_table'][0][4]
  plantPrice = data['basket_table'][0][3]
  document.getElementById('item_name').innerHTML = plantName;
  document.getElementById('item_quantity').innerHTML = plantQuantity;
  document.getElementById('item_price').innerHTML = plantPrice;
  
}
displayBasket();

