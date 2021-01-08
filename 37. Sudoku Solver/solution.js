/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function(board) {
  for (let x = 0; x < 9; x++)
    for (let y = 0; y < 9; y++)
      if (board[x][y] === ".") {
        for (let val = 1; val <= 9; val++)
          if (valid(board, x, y, val.toString())) {
            board[x][y] = val.toString();
            if (solveSudoku(board)) return true;
            board[x][y] = ".";
          }
        return false;
      }
  return true;
};

var valid = (board, x, y, val) => {
  for (let i = 0; i < 9; i++) {
    const m = 3 * Math.floor(x / 3) + Math.floor(i / 3);
    const n = 3 * Math.floor(y / 3) + (i % 3);
    if (board[x][i] === val || board[i][y] === val || board[m][n] === val)
      return false;
  }
  return true;
};
