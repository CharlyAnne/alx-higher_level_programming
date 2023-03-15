const bill = 275 ;
const tip = bill >= 50 && bill <= 300 ? (15 * bill) / 100 : bill * .20; 
console.log(tip);
console.log(`the bill was ${bill} and the tip was ${tip}. Hence the total is 
${bill + tip}`)