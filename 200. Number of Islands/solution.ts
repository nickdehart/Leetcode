function validPosition(grid: string[][], rowIndex: number, colIndex: number) :boolean {

	// row index in bounds
	const rowLength = grid.length;
	if(rowIndex < 0) return false;
	if(rowIndex > rowLength-1) return false;

	// col index in bounds
    const colLength = grid[rowIndex].length;
	if(colIndex < 0) return false;
	if(colIndex > colLength-1) return false;

	// haven't hit water
	if(grid[rowIndex][colIndex] === '0') return false;
	return true;
}


function search(grid: string[][], rowIndex: number, colIndex: number) :void {
	if(validPosition(grid, rowIndex, colIndex)) {
		grid[rowIndex][colIndex] = '0';
		search(grid, rowIndex-1, colIndex); // north
		search(grid, rowIndex+1, colIndex); // south
		search(grid, rowIndex, colIndex+1); // east
		search(grid, rowIndex, colIndex-1); // west
	}
}


function numIslands(grid: string[][]) :number {
	let count = 0;

	for (let r = 0; r < grid.length; r++) 
		for (let c = 0; c < grid[r].length; c++) 
			if(grid[r][c] === '1') {
				count += 1;
				search(grid, r, c);
			}

    return count;
}
