function solution(survey, choices) {
  const surveyOrder = ["R", "T", "C", "F", "J", "M", "A", "N"];
  const surveyScore = Array(8).fill(0);
  let answer = "";

  survey.forEach((item, index) => {
    let surveyType = item.split("");
    if (choices[index] - 4 < 0) {
      surveyScore[surveyOrder.indexOf(surveyType[0])] += Math.abs(
        choices[index] - 4
      );
    } else if (choices[index] - 4 > 0) {
      surveyScore[surveyOrder.indexOf(surveyType[1])] += choices[index] - 4;
    }
  });

  surveyScore.forEach((_item, i, arr) => {
    if (i % 2 == 0) {
      if (arr[i] >= arr[i + 1]) {
        answer += surveyOrder[i];
      } else if (arr[i] < arr[i + 1]) {
        answer += surveyOrder[i + 1];
      }
    }
  });

  return answer;
}
