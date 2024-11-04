let input = "1S18D*2T";

function calculator(dartResult) {
  const bonus = { S: 1, D: 2, T: 3 };
  let scores = []; // 각 점수(보너스 계산 후에)를 저장할 배열
  let num = ""; // 입력받은 다트 결과의 숫자인 요소를 집어넣을거임

  for (let i = 0; i < dartResult.length; i++) {
    if (!isNaN(dartResult[i])) {
      // 현재 문자가 숫자인지 확인
      num += dartResult[i];
    } else if (bonus[dartResult[i]]) {
      scores.push(Math.pow(Number(num), bonus[dartResult[i]]));
      num = 0;
    } else if (dartResult[i] === "*") {
      scores[scores.length - 1] *= 2;
      if (scores.length > 1) scores[scores.length - 2] *= 2; // 이전 점수가 있으면 걔도 x2
    } else if (dartResult[i] === "#") {
      scores[scores.length - 1] *= -1;
    }
  }

  return scores.reduce((acc, cur) => acc + cur, 0);
}

calculator(input);
