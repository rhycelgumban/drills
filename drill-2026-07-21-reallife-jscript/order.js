// REAL LIFE EXAMPLE: ORDER PAGKAON
// Kung may kwarta,
// maka-order ko.
// Kung wala,
// tan-awon ko kung may libre.
// Kung may libre,
// kaon gihapon.
// Kung wala,
// tubig na lang danay.

const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("May kwarta ka? (huo/wala): ", (answer) => {

    const mayKwarta = answer.toLowerCase() === "huo";

    if (mayKwarta) {
        console.log("Order na ta!");
        rl.close();
    } else {
        rl.question("Libre mo? (huo/nd): ", (answer) => {

            const libre = answer.toLowerCase() === "huo";

            if (libre) {
                console.log("Libre is life!");
            } else {
                console.log("Tubig na lang ta danay.");
            }

            rl.close();
        });
    }
});