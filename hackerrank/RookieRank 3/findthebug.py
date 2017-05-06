def find_bug(matrix):
	row_count =  0
	for row in matrix:
		if 'X' in row:
			return row_count, row.find('X')
		row_count += 1

if __name__ == '__main__':
	grid_size = int(input())
	matrix = [str(input()) for row in range(grid_size)]
	a, b = find_bug(matrix)
	print (a, b)