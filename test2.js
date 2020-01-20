function pyramidCoinChange(cointypes) {
    // save the coin types in coins
    // add pyramid form to coins
    this.coins = cointypes.sort((a, b) => a + b);
    this.numCoinTypes = this.coins.length;
}
pyramidCoinChange.prototype = {
    // pass amount to this function
    generateCoins(amount) {
        var finalresult = [],
            totalAmount = amount;
        // loop through the coin types. for each type find how many 
        // of the amount you can get 
        for (var i = 0; i < this.numCoinTypes; i++) {
            // first get the value of the coin type
            var currentTypeValue = this.coins[i],
            // count the number of that type of coin.
            // by calculating the currentTypeValue over totalAmount
            typeCount = Math.floor(totalAmount / currentTypeValue);
            // push the coin count into result
            finalresult.push(typeCount);
            // update the total amount so on the next iteration we can find the right
            // type count
            totalAmount -= (currentTypeValue * typeCount);
        }
        // return the final results
        return finalresult;
    },
    // display the list of coins generated 
    displayResults(amount){
        var results = this.generateCoins(amount);
        console.log(results);
        for(var i = 0; i < results.length; i++) {
            console.log('There are( '+results[i]+' ) ', this.coins[i], ' Naira');
        }
    }
};

var cointypes = [25, 10, 7, 2],
    coinChanger = new pyramidCoinChange(cointypes);
coinChanger.displayResults(191);

// Dynamic Programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems,
// solving each of those subproblems just once, and storing their solutions using a memory-based data structure (array, map,etc).

// A greedy algorithm is a simple, intuitive algorithm that is used in optimization problems.
// The algorithm makes the optimal choice at each step as it attempts to find the overall optimal way to solve the entire problem.

// pyramid form is a form
// in which information is presented in descending order of importance. 
// This allows the audience to read the most crucial details quickly 
// so they can decide whether to continue or stop reading the story.

// before going through the loop i arranged the coins in pyramid form
// after wards i got the value of the coin type
// counted the number of that type of coin.
// by calculating the currentTypeValue over totalAmount
// push the coin count into result
// update the total amount so on the next iteration i found the right
// type count
// return the final results
// display the list of coins generated 