// Page Animations
window.addEventListener("beforeunload", function () {
  document.body.classList.add("animate-out");
});

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

// list of your plants (should match database)
plantsList = ['bonsai', 'peace_lily', 'aloe_vera', 'monstera_deliciosa', 'cactus', 'spider_plant', 'snake_plant', 'devils_ivy',  'olive_tree', 'lemon_tree', 'palm_tree']
// list of your plant quantities (to be filled by for loop)
plantsQuantities = []

// For loop to retreive quantities for all plants in the list
for(i = 0; i < (plantsList).length; i++  ){
  quantity = httpGet(`http://127.0.0.1:5000/plants_data/${plantsList[i]}/quantity`);
  plantsQuantities.push(quantity)
}

function displayStock() {
  for(i = 0; i < (plantsList).length; i++ ) {
    console.log(plantsList[i]);
    document.getElementById(`${plantsList[i]}-stock`).innerHTML = plantsQuantities[i] + " available";
  }
}

displayStock();


// Buy button - when clicked it will reduce the chosen stock quantity by 1
// function buyStockButton(plantName) {
//   httpGet(`http://127.0.0.1:5000/plants_data/${plantName}/purchase`);
//   location.reload();
// }

// function that triggers api add to basket function given parameters
function addToBasket(plantName) {
  console.log(plantName)
  quantity = document.getElementById(`quantitySelectorButton-${plantName}`).value;
  console.log(quantity)
  httpGet(`http://127.0.0.1:5000/basket/${plantName}/${quantity}/cartid`);
  location.reload();
}
// displays basket quantities in basket icon
function displayBasketQuantity() {
  basketQuantity = httpGet(`http://127.0.0.1:5000/basket_table_data/all_items_quantity`)
  document.getElementById('lblCartCount').innerHTML = basketQuantity;
}

displayBasketQuantity();
