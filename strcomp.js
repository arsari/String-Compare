///  node terminal prompt-sync package require
var prompt = require('prompt-sync')();
var colors = require('colors');

// function declaration
function strCompare(str1, str2) {
    var str1Array = str1.split('');
    var str2Array = str2.split('');
    if (str1.length === str2.length) {
        if (str1.localeCompare(str2) === 0) {
            return 'equal';
        } else if (str1Array.sort().join() == str2Array.sort().join()) {
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
};

// input loop
while (true) {
    // script description and user input prompt
    console.log('\n====================================='.red + 'v1.0.170309'.yellow);
    console.log('This JS script will compare two strings to\ndetermine if both are equal in length, letters,\nand world...'.cyan + '\n' + '(For exit, press Enter in any of the inputs.)'.gray);
    console.log('------------------------------------------------'.blue);
    var userStr1 = prompt('Enter a First String value: '.italic.yellow);
    var userStr2 = prompt('Enter a Second String value: '.italic.yellow);
    console.log('================================================\n'.red);

    // user inputs evaluation
    if (Number(userStr1) === 0 || Number(userStr2) === 0) {
        console.log('-----------------'.bgMagenta);
        console.log('|'.bgMagenta + '  Good Bye!!!  ' + '|'.bgMagenta);
        console.log('-----------------'.bgMagenta + '\n');
        return;
    } else if (isNaN(userStr1) == false || isNaN(userStr2) == false) {
        console.log(' *** INPUT ERROR *** '.bgRed + '\n' + ' Input value should be a String. '.bgRed);
    } else {
        // call function
        var compareResult = strCompare(userStr1, userStr2);

        // console outputs
        if (compareResult == 'equal') {
            console.log(' String(1) and String(2) is the same string. '.white.bgBlue + '\n');
            return;
        } else if (compareResult) {
            console.log(' String(1) and String(2) are equal in lenght and containg the same letters. '.white.bgGreen + '\n');
            return;
        } else {
            console.log(' String(1) and String(2) are different strings. '.red.bgYellow + '\n');
            return;
        }
    }
}
