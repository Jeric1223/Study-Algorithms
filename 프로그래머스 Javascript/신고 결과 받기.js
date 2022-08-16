function solution(id_list, report, k) {
  const answer = Array(id_list.length).fill(0);
  // 신고자가 신고한 내역들을 넣는 배열
  const reportedArr = Array.from(Array(id_list.length), () => new Array(0))
  // 신고된 횟수를 체크하는 배열 (사람의 순서는 id_list의 순서로)
  const reportCountArr = Array(id_list.length).fill(0)
  
  report.forEach((value, index) => {
      // splitString[0]은 신고자, splitString[1]은 피신고자
      let splitString = value.split(' ')
      
      // 똑같은 사람을 신고하지 않았으면 자신의 신고 내역에 추가하고 총 신고 횟수를 추가한다. 
      if(reportedArr[id_list.indexOf(splitString[0])].includes(splitString[1]) === false ) {
          reportedArr[id_list.indexOf(splitString[0])].push(splitString[1]) 
          reportCountArr[id_list.indexOf(splitString[1])] += 1
      }
  })
  
  reportedArr.forEach((arr,index) => {
      arr.forEach((item) => {
          if(reportCountArr[id_list.indexOf(item)] >= k) {
              answer[index]++
          }
      })
  }) 
  
 return answer
}
