function solution(numbers) {
  var answer = [];

  for (let i = 0; i < numbers.length; i++) {
    numbers.forEach((item, index, arr) => {
      if (answer.includes(arr[i] + item) === false) {
        if (i != index) {
          answer.push(arr[i] + item);
        }
      }
    });
  }
  return answer.sort((a, b) => {
    return a - b;
  });
}
