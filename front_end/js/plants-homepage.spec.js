const { expect } = require('@jest/globals');
const fs = require('fs');
const path = require('path');
const html = fs.readFileSync(path.resolve(__dirname, '../html/plants-homepage.html'), 'utf8');
const { displayStock, displayBasketQuantity } = require('./plants-homepage');

jest
    .dontMock('fs');

describe('button', function () {
    beforeEach(() => {
        document.documentElement.innerHTML = html.toString();
        // html_element = document.getElementById('buy-button')
        // console.log(html_element.innerHTML)
    });

    afterEach(() => {
        // restore the original func after test
        jest.resetModules();
    });


    test('displays plant stock and quantities available', function () {
        // given: a list of plants and list of quantities
        plantsList = ['bonsai', 'peace_lily']
        plantsQuantities = [100, 85]
        
        // when: I run my display stock function
        displayStock(plantsList, plantsQuantities);

        // then: the innerHTML of the plants in the plants list are updated 
        // with the correct quantity from the quantities list
        bonsaiStockInnerHTML = document.getElementById('bonsai-stock').innerHTML;
        peaceLilyStockInnerHTML = document.getElementById('peace_lily-stock').innerHTML;
        
        expect(bonsaiStockInnerHTML).toBe("100 available");
        expect(peaceLilyStockInnerHTML).toBe("85 available");
    });

});

// function displayStock() - displays all available stock in the HTML
// function addToBasket(plantName) - probably don't want to test this as it is triggers the api rather than changes the browser
// function displayBasketQuantity() - displays basket quantity in the HTML as a basket icon