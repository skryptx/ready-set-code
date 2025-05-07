console.log(x);
// console.log(y); // Will Error out - No Hosting - Temporal Dead zone
console.log(getName());

var x = 10;
let y = 20;
function getName() {
  return "Sinni";
}
