class CountSquares:

    def __init__(self):
        self.point_count = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.point_count[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point[0],point[1]
        res = 0

        for x,y in self.points:
            if x == px or y == py or (abs(py - y) != abs(px - x)):
                continue # if we're looking at the same point OR the 2 (x,y) points arent diagonal -> continue
            res += self.point_count[(x,py)] * self.point_count[(px,y)]
        return res
