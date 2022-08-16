function solution(strings, n) {
  var answer = [];
  let newArr = [];

  strings.forEach((item) => {
    newArr.push(`${item[n]}${item}`);
  });

  newArr.sort();

  newArr.forEach((item) => {
    answer.push(item.slice(1));
  });

  return answer;
}
