class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        result = []
        visited = set()

        # right, down, left, up
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        def dfs(r: int, c: int, direction: int) -> None:
            visited.add((r, c))
            result.append(matrix[r][c])

            if len(result) == rows * cols:
                return

            dr, dc = directions[direction]
            nr, nc = r + dr, c + dc

            # Turn if the next cell is invalid or already visited
            if (
                nr < 0 or nr >= rows or
                nc < 0 or nc >= cols or
                (nr, nc) in visited
            ):
                direction = (direction + 1) % 4
                dr, dc = directions[direction]
                nr, nc = r + dr, c + dc

            dfs(nr, nc, direction)

        dfs(0, 0, 0)
        return result