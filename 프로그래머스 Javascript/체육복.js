function solution(n, lost, reserve) {
  var answer = 0;

  // 서로의 배열에 대한 차집합을 새로운 배열에 저장 (여분이 있을때 도난 당하는 경우의 수 제거 )
  let diffLost = lost.filter((x) => !reserve.includes(x));
  let diffReserve = reserve.filter((y) => !lost.includes(y));

  // 총 잃어버린 숫자
  let lostLen = diffLost.length;

  diffLost.sort();

  diffLost.forEach((lostItem) => {
    if (diffReserve.includes(lostItem - 1)) {
      //나보다 왼쪽에 빌려줄 사람이 있으면
      answer += 1;
      diffReserve = diffReserve.filter((item) => item !== lostItem - 1);
    } else if (diffReserve.includes(lostItem + 1)) {
      //나보다 오른쪽에 빌려줄 사람이 있으면
      answer += 1;
      diffReserve = diffReserve.filter((item) => item !== lostItem + 1);
    }
  });

  return n - lostLen + answer;
}