function httpGet(theUrl) {
  let xmlHttpReq = new XMLHttpRequest();
  xmlHttpReq.open("GET", theUrl, false); 
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
    document.getElementById(`${plantsList[i]}-stock`).innerHTML = plantsQuantities[i] + " available";
  }
}

displayStock();