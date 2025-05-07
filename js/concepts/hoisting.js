/*
Explanation on code execution:
Js engine allocates memory in first run and executes code in second run.
All variables(initialized with var) are assigned undefined in first run and functions are stored as is.

That means, variables will be undefined if accessed before definition, but functions can be called
as is without any impact.
*/

console.log(x);
// console.log(y); // Will Error out - No Hosting - Temporal Dead zone
console.log(getName());

var x = 10;
let y = 20;
// functions are stored as is, so they can be called anywhere, even before the definition
function getName() {
  return "Sinni";
}
