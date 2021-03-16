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
  plantData = data['basket_table']
  
  // document.getElementById('item_pic').src='images/' + plantImage;
  // document.getElementById('item_name').innerHTML = plantName;
  // document.getElementById('item_quantity').innerHTML = plantQuantity;
  // document.getElementById('item_price').innerHTML = '£' + plantPrice * plantQuantity;
  // Find a <table> element with id="myTable":
  var table = document.getElementById("basket_table");

// For loop to loop through items in the basket table. Creates new cells to import data into.
  for (i = 0; i < plantData.length; i++) {
    let plantName = plantData[i][1]
    let plantQuantity = plantData[i][4]
    let plantPrice = plantData[i][3]
    let plantImage = "images/img_" + plantName + ".jpg"

  
    
  // Create an empty <tr> element and add it to the 1st position of the table:
    var row = table.insertRow(i+1);

    // Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
    var pictureCell = row.insertCell(0);
    var nameCell = row.insertCell(1);
    var quantityCell = row.insertCell(2);
    var priceCell = row.insertCell(3);

    // Add some text to the new cells:
    pictureCell.innerHTML="<img src='" + plantImage + "' alt='" + plantName + " img missing'/>";
    nameCell.innerHTML = replaceUnderscore(plantName);
    quantityCell.innerHTML = plantQuantity;
    priceCell.innerHTML = '£' +plantPrice;

    }
  
}
displayBasket();


// Change instances of underscores to spaces and capitalise first letter of word
function replaceUnderscore(plantName) {
  plantName = plantName.replaceAll('_', ' ');
  return plantName.charAt(0).toUpperCase() + plantName.slice(1);
}