def n_queens(n):
    def solve_n_queens(row):
        if row == n:
            # All queens are legally placed.
            result.append(col_placement.copy())
            return
        for col in range(n):
            # Test if a newly place queen will conflict any earlier queens place before
            # Check the condition for the already existing queens on the table
            # diagonal, vertical, orizontal lines
            # c - col == 0 -> conflict in the columns
            # c - col == i - row -> conflict diagonal up/ left
            # c - col == row - i -> conflict diagonal up/ right
            if all(abs(c - col) not in (0, row - i)
                for i, c in enumerate(col_placement[:row])):
                    col_placement[row] = col
                    solve_n_queens(row + 1)

    result = []
    col_placement = [0] * n
    solve_n_queens(0)
    return result

def nr_n_queens(n):
    print(len(n_queens(n)))

nr_n_queens(4)
