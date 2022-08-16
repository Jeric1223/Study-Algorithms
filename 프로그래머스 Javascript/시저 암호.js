function solution(s, n) {
  //문자열.charCodeAt(문자열 자릿수) /String.fromCharCode(아스키코드 번호)
  var answer = [];
  let stringArr = s.split("");
  let temp = 0;

  stringArr.forEach((item, index) => {
    if (item === " ") {
      answer.push(item);
    } else if (item.charCodeAt() >= 65 && item.charCodeAt() <= 90) {
      //대문자 범위
      if (item.charCodeAt() + n > 90) {
        //대문자 범위를 넘어가면
        temp = item.charCodeAt() + n - 90;
        answer.push(String.fromCharCode(64 + temp));
      } else {
        answer.push(String.fromCharCode(item.charCodeAt() + n));
      }
    } else if (item.charCodeAt() >= 97 && item.charCodeAt() <= 122) {
      // 소문자 범위
      if (item.charCodeAt() + n > 122) {
        //소문자 범위를 넘어가면
        temp = item.charCodeAt() + n - 122;
        answer.push(String.fromCharCode(96 + temp));
      } else {
        answer.push(String.fromCharCode(item.charCodeAt() + n));
      }
    }
  });
  return answer.join("");
}