# Kiểm tra xem trạng thái puzzle có thể giải được hay không
def isSolvable(puzzle):
    flatPuzzle = [num for row in puzzle for num in row if num != 0]
    inversions = sum(
        1 for i in range(len(flatPuzzle)) for j in range(i + 1, len(flatPuzzle))
        if flatPuzzle[i] > flatPuzzle[j]
    )
    return inversions % 2 == 0 