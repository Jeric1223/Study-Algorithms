function solution(s) {
  let stringArr = s.split(" ");
  var newArr = [];
  let answer = [];

  for (let i = 0; i < stringArr.length; i++) {
    newArr.push([]);
  }

  stringArr.forEach((item, index_1) => {
    [...item].forEach((stringItem, index_2) => {
      if (index_2 % 2 == 0) {
        newArr[index_1].push(stringItem.toUpperCase());
      } else {
        newArr[index_1].push(stringItem.toLowerCase());
      }
    });
  });

  newArr.forEach((item) => {
    answer.push(item.join(""));
  });

  return answer.join(" ");
}