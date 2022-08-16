function solution(board, moves) {
  var answer = 0;
  let stackArr = []
  let pick = 0
  let boardQue = []
  
  for(let j = 0; j < board[0].length; j++) {
      boardQue.push([])
  }
  
  board.forEach(item => {
      item.forEach((childItem, childIndex) => {
          if(childItem !== 0) {
              boardQue[childIndex].push(childItem)
          }
      })
  })
  
  for(let i = 0; i < moves.length; i++) {
      pick = boardQue[moves[i]-1].shift();
      if(pick != undefined) {
          stackArr.push(pick)
      }

      if(stackArr.length >= 2) {
          if(stackArr[stackArr.length - 1] === stackArr[stackArr.length - 2]){
              stackArr.pop()
              stackArr.pop()
              answer += 2
          }
      }
  }
  
  return answer;
}