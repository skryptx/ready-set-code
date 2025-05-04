class Person {
  name = "";
  dept = "";
  constructor(name = "", dept = "") {
    this.name = name;
    this.dept = dept;
  }

  greet() {
    console.log(`Hello, ${this.name}!`);
    console.log(this);
  }

  showDept = () => {
    console.log(`Dept: ${this.dept}`);
    console.log(this);
  };
}

const sinni = new Person("sinni", "cs");
sinni.greet();
sinni.showDept();
console.log(this);
