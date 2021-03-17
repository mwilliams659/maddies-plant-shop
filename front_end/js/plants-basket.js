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

// All of the plants in the database
plantsList = ['bonsai', 'peace_lily', 'aloe_vera', 'monstera_deliciosa', 'cactus', 'spider_plant', 'snake_plant', 'devils_ivy',  'olive_tree', 'lemon_tree', 'palm_tree']


  // displays basket quantities in basket icon
function displayBasketQuantity() {
    basketQuantity = httpGet(`http://127.0.0.1:5000/basket_table_data/all_items_quantity`)
    document.getElementById('lblCartCount').innerHTML = basketQuantity;
    }
  
  displayBasketQuantity();


// Delete item from basket table and put back into plants data database
function deleteItemFromBasket(cart_id, plant_name) {
  httpGet(`http://127.0.0.1:5000/basket/${cart_id}/${plant_name}/removeitem`);
  location.reload();


}

//  Display All Basket Table Data

function displayBasket() {
  allBasketData = httpGet(`http://127.0.0.1:5000/basket_table_data`)
  // console.log(basketData['basket_table'])
  let data = JSON.parse(allBasketData);
  // console.log(data['basket_table'][0]) - this displays the arrays in the baskettable. Uses the index to access the values.
  plantData = data['basket_table']
  
  var table = document.getElementById("basket_table");
  if (plantData.length > 0) {
    table.style.display = "block";
    let subTotal = 0;

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
        var deleteCell = row.insertCell(4);
    
        // Add some text to the new cells:
        pictureCell.innerHTML="<img src='" + plantImage + "' alt='" + plantName + " img missing'/>";
        nameCell.innerHTML = replaceUnderscore(plantName);
        quantityCell.innerHTML = plantQuantity;
        priceCell.innerHTML = '£' +plantPrice;
        deleteCell.innerHTML = `<button class="deleteButton" onclick="deleteItemFromBasket('cartid', '${plantName}')"><i class="fa fa-trash" title="Delete item from basket" style="font-size:36px"></i></button>`;
    
    
    
        subTotal = subTotal + plantPrice;
      
    
        }
      document.getElementById("subtotal").innerHTML = "Subtotal: £" + subTotal;  
  } else {
    document.getElementById("emptyBasket").innerHTML = "Your basket is currently empty.";
  }


};

displayBasket();


// Change instances of underscores to spaces and capitalise first letter of word
function replaceUnderscore(plantName) {
  plantName = plantName.replaceAll('_', ' ');
  return plantName.charAt(0).toUpperCase() + plantName.slice(1);
}

