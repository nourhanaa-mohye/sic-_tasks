
//1. Hello World: Write a program to print "Hello, World!" to the console.
console.log("Hello, World!");

//2. Reverse String: Write a function that takes a string and returns it reversed.

function reverseString(str) {
    return str.split('').reverse().join('');
  }
  
  const userInput = prompt('Enter a string:');
  const reversedString = reverseString(userInput);
  console.log(reversedString);
//3. Factorial: Write a function to find the factorial of a given number.
function factorial(number):{
    const number = parseInt(prompt('Enter a positive integer: '));
    if (number < 0) {
        console.log('Error! Factorial for negative number does not exist.');
    }
    else if (number === 0) {
        console.log(`The factorial of ${number} is 1.`);
    }

    else {
        let fact = 1;
        for (i = 1; i <= number; i++) {
            fact *= i;
        }
        console.log(`The factorial of ${number} is ${fact}.`);
    }} return;
}
//4. Sum Array: Write a function that takes an array of numbers and returns their sum.
function sumArray(numbers) {
    let sum = 0;
    for (let i = 0; i < numbers.length; i++) {
      sum += numbers[i];
    }
    return sum;
  }
  const userInput = prompt('Enter numbers separated by commas:');
  const numberArray = userInput.split(',').map(Number);
  const arraySum = sumArray(numberArray);
  console.log(arraySum);
//5. Palindrome: Write a function that checks whether a given word or phrase is a palindrome.
function isPalindrome(str) {
    const cleanedStr = str.toLowerCase().replace(/[^a-zA-Z0-9]/g, '');
    const reversedStr = cleanedStr.split('').reverse().join('');
    return cleanedStr === reversedStr;
  }

  const userInput = prompt('Enter a word or phrase:');
  const result = isPalindrome(userInput);
  
  if (result) {
    console.log('It is a palindrome.');
  } else {
    console.log('It is not a palindrome.');
  }
//6. Odd or Even: Write a function that tells if a number is odd or even.
function checkOddOrEven(number) {
    if (number % 2 === 0) {
      return 'Even';
    } else {
      return 'Odd';
    }
  }
  const userInput = prompt('Enter a number:');
  const number = parseInt(userInput);
  const result = checkOddOrEven(number);
  console.log(result);


//7. Fibonacci Series: Write a function that returns the first n numbers of the Fibonacci sequence.
function fibonacciSeries(n) {
    const series = [0, 1];
  
    if (n <= 2) {
      return series.slice(0, n);
    }
  
    for (let i = 2; i < n; i++) {
      const nextNumber = series[i - 1] + series[i - 2];
      series.push(nextNumber);
    }
    return series;
  }
  const userInput = prompt('Enter the number of Fibonacci numbers:');
  const count = parseInt(userInput);
  const result = fibonacciSeries(count);
  console.log(result);



