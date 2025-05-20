const obj = {
  value: 42,
  getValue: function () {
    console.log(this);
    return this.value;
  },
};

const getVal = obj.getValue;
console.log(getVal());
