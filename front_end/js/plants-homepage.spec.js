const fs = require('fs');
const path = require('path');
const html = fs.readFileSync(path.resolve(__dirname, '../html/plants-homepage.html'), 'utf8');

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

    it('button exists', function () {
        expect(document.getElementById('buy-button').innerHTML).toBe("↓↓↓↓↓↓ Here is your InnerHTML");
    });
});