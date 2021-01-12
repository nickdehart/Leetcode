/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
  for (let x = 0; x < 9; x++)
    for (let y = 0; y < 9; y++)
      if (board[x][y] !== ".") {
        for (let i = 0; i < 9; i++) {
          const m = 3 * Math.floor(x / 3) + Math.floor(i / 3);
          const n = 3 * Math.floor(y / 3) + (i % 3);
          if (
            (board[x][i] === board[x][y] && y !== i) ||
            (board[i][y] === board[x][y] && i !== x) ||
            (board[m][n] === board[x][y] && m !== x && n !== y)
          )
            return false;
        }
      }
  return true;
};
