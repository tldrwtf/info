// Practice_Solutions/JavaScript/JavaScript_Object_Access_Solutions.js

// Task 15.4: Object Access

const car = {
    make: "Toyota",
    model: "Corolla",
    year: 2020,
    features: ["AC", "Radio", "Bluetooth"]
};

// 1. Log the make and model combined.
console.log(`\nCar: ${car.make} ${car.model}`); // Expected: Car: Toyota Corolla

// 2. Loop through features and log each one.
console.log("Features:");
car.features.forEach(feature => {
    console.log(`- ${feature}`);
});
/* Expected:
- AC
- Radio
- Bluetooth
*/

// 3. Add a new property mileage with value 50000.
car.mileage = 50000;
console.log("\nCar object after adding mileage:", car);
/* Expected (mileage property added):
{
  make: 'Toyota',
  model: 'Corolla',
  year: 2020,
  features: [ 'AC', 'Radio', 'Bluetooth' ],
  mileage: 50000
}
*/
