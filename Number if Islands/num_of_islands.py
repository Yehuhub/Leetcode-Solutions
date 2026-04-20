"""
 what we actually do here is doing bfs on each element in the matrix that is 1,
 if it is in visited it means we have looked into that island already,
 if not we call bfs on it to find all the 1's that are connected to it, that way
 each run of bfs will insert all adjacent land into the visited set
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROW_SIZE = len(grid)
        COL_SIZE = len(grid[0])
        island_count = 0

        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            dirs = [[1,0], [-1,0], [0,1], [0,-1]]

            while q:
                i, j = q.popleft()

                for dr, dc in dirs:
                    row = i + dr
                    col = j + dc
                    if row < 0 or col < 0 or row >= ROW_SIZE or col >= COL_SIZE:
                        continue
                    if grid[row][col] == "1" and (row,col) not in visited:
                        visited.add((row,col))
                        q.append((row,col))


        for r in range(ROW_SIZE):
            for c in range(COL_SIZE):
                if grid[r][c] == "1" and (r,c) not in visited:
                    island_count += 1
                    bfs(r,c)

        return island_count

