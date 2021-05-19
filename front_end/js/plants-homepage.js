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

// list of your plants (should match database)
plantsList = ['bonsai', 'peace_lily', 'aloe_vera', 'monstera_deliciosa', 'cactus', 'spider_plant', 'snake_plant', 'devils_ivy',  'olive_tree', 'lemon_tree', 'palm_tree']
// list of your plant quantities (to be filled by for loop)
plantsQuantities = []

// For loop to retreive quantities for all plants in the list
for(i = 0; i < (plantsList).length; i++  ){
  quantity = httpGet(`http://127.0.0.1:5000/plants_data/${plantsList[i]}/quantity`);
  plantsQuantities.push(quantity)
}

// Displays all available stock
function displayStock(plantsList, plantsQuantities) {
  for(i = 0; i < (plantsList).length; i++ ) {
    console.log(plantsList[i])
    document.getElementById(`${plantsList[i]}-stock`).innerHTML = plantsQuantities[i] + " available";
  }
}

// displayStock(plantsList, plantsQuantities);


// function that triggers api add to basket function given parameters
function addToBasket(plantName) {
  quantity = document.getElementById(`quantitySelectorButton-${plantName}`).value;
  httpGet(`http://127.0.0.1:5000/basket/${plantName}/${quantity}/cartid`);
  location.reload();
}
// displays basket quantities in basket icon
function displayBasketQuantity() {
  basketQuantity = httpGet(`http://127.0.0.1:5000/basket_table_data/all_items_quantity`)
  document.getElementById('lblCartCount').innerHTML = basketQuantity;
}

// displayBasketQuantity();


// particles background
function startParticles() {
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
}


window.onload =
  displayStock(plantsList, plantsQuantities);
  displayBasketQuantity();
  startParticles();


module.exports = { displayStock, displayBasketQuantity };
