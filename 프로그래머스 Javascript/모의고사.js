function solution(answers) {
  var answer = [];
  let frist_person = [1,2,3,4,5]
  let second_person = [2,1,2,3,2,4,2,5]
  let third_person = [3,3,1,1,2,2,4,4,5,5]
  let score_arr = [0,0,0]
  let max = 0
  
  answers.forEach((item, index) => {
      if(item == frist_person[index%5]){
          score_arr[0] += 1
      }
      if(item == second_person[index%8]){
          score_arr[1] += 1
      }
      if(item == third_person[index%10]){
          score_arr[2] += 1
      }
  })
  
  score_arr.forEach(item => {
      if(max < item){
          max = item
      }
  })
  
  score_arr.forEach((item,index) => {
      if(max == item){
          answer.push(index+1)
      }
  })
  
  return answer;
}