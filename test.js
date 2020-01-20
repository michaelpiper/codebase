let cache =[],db=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on("close", function() {
    console.log("\nBYE BYE !!!");
    process.exit(0);
});
function findFromCacheOrDB(){  
    rl.question("Enter a value to find:", function(find) {
        find=find;
        continueFind(find);
    });
    var continueFind=(find)=>{
        var promise1 = new Promise(function(resolve, reject) {
            // something that fails
            for (var i in cache){
                if(cache[i]==find){
                 resolve("found from cache "+find);
                }
            }
            // setTimeout(() => reject(new Error("Whoops!")), 700);
        });
        var promise2 = new Promise(function(resolve, reject) {
            // something that succeeds
            for (var i in db){
                if(db[i]==find){
                    cache.push(db[i]);
                    resolve("found from db");
                    break;
                }
            }
            reject(new Error("Whoops couldn't found in database or cache!"));
        });
    
        return Promise.race([promise1, promise2])
        .then(function(value) {
            // Use whatever returns fastest
            console.log(value);
            findFromCacheOrDB();
        })
        .catch(function(reason) {
            console.log(reason);
            findFromCacheOrDB();
        });
    }
}
console.log('enter control c to stop');
console.log('enter from a list of '+ db.join(', '));
findFromCacheOrDB();


//  A promise is commonly defined as a proxy for a value that will eventually become available.
//  Promises are one way to deal with asynchronous code, without getting stuck in callback hell.

//  No you shouldn't implement this code in your app
//  because Promise.race() method returns a promise that fulfills or
//  rejects as soon as one of the promises in an iterable fulfills 
//  or rejects, with the value or reason from that promise.
//  hence Promise.race is able to solve the latency problem

//  As you can see from the above solution, the promise checks the cache global variable, and if the data is found in it,
//  the promise goes to a resolved state (since the resolve callback was called) and it return to the then block;
//  but if the data is not found in the cache memory it goes to promise2 to check the database,
//  and if the data is found in it 
//  the promise2 goes to resolved state and add the data to cache memory and it return to the then block. 
//  so if the data also is not found in database then it rejects,
//  which means the promise goes to reject state (since the reject callback was called) and it return to catch block
//  but if it was a function call it will reject as soon as the data is not found in cache
