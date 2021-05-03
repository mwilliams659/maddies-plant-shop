// Page Animations
window.addEventListener("beforeunload", function () {
    document.body.classList.add("animate-out");
  });



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
    
    
    
        subTotal = Number(subTotal);
        subTotal = subTotal + plantPrice * plantQuantity;
      
    
        }
      document.getElementById("subtotal1").innerHTML = "Subtotal (excluding delivery):";
      document.getElementById("delivery1").innerHTML = "Delivering to:";
      document.getElementById("payment1").innerHTML = "UK Standard delivery:";
      document.getElementById("total1").innerHTML = "Total (including delivery):";
      document.getElementById("subtotal2").innerHTML = "£" + subTotal.toFixed(2);
      document.getElementById("delivery2").innerHTML = "United Kingdom";
      document.getElementById("payment2").innerHTML = "£4.00";
      totalWithDelivery = parseFloat(subTotal + 4);
      document.getElementById("total2").innerHTML = "£" + totalWithDelivery.toFixed(2);
      document.getElementById("checkout").innerHTML = "CHECKOUT";
      document.getElementById("iconContainer").style.display = "block";

  } else {
    document.getElementById("emptyBasket").innerHTML = "There are currenty no items in your basket.";
    document.getElementById("summary").style.display = "none";
    document.getElementById("checkout").style.display = "none";
  }


};

displayBasket();


// Change instances of underscores to spaces and capitalise first letter of word
function replaceUnderscore(plantName) {
  plantName = plantName.replaceAll('_', ' ');
  return plantName.charAt(0).toUpperCase() + plantName.slice(1);
}



// particles background
particlesJS("particles-js", {
  particles: {
    number: { value: 4, density: { enable: true, value_area: 800 } },
    color: { value: "#4caf50" },
    shape: {
      type: "polygon",
      stroke: { width: 0, color: "#000" },
      polygon: { nb_sides: 6 },
      image: { src: "img/github.svg", width: 100, height: 100 }
    },
    opacity: {
      value: 0.3,
      random: true,
      anim: { enable: false, speed: 1, opacity_min: 0.1, sync: false }
    },
    size: {
      value: 91.9080919080919,
      random: false,
      anim: { enable: true, speed: 10, size_min: 40, sync: false }
    },
    line_linked: {
      enable: false,
      distance: 200,
      color: "#ffffff",
      opacity: 1,
      width: 2
    },
    move: {
      enable: true,
      speed: 4.795204795204795,
      direction: "none",
      random: false,
      straight: false,
      out_mode: "out",
      bounce: false,
      attract: { enable: false, rotateX: 600, rotateY: 1200 }
    }
  },
  interactivity: {
    detect_on: "canvas",
    events: {
      onhover: { enable: false, mode: "grab" },
      onclick: { enable: false, mode: "push" },
      resize: true
    },
    modes: {
      grab: { distance: 400, line_linked: { opacity: 1 } },
      bubble: { distance: 400, size: 40, duration: 2, opacity: 8, speed: 3 },
      repulse: { distance: 200, duration: 0.4 },
      push: { particles_nb: 4 },
      remove: { particles_nb: 2 }
    }
  },
  retina_detect: true
});

update = function () {

  requestAnimationFrame(update);
};
requestAnimationFrame(update);
