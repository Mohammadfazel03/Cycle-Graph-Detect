class Vertices:
    def __init__(self, start_edge: int, destination_edge: int):
        self.start_edge = start_edge
        self.destination_edge = destination_edge
        self.visited = False


def is_cycle(graph: list, start_point: Vertices = None, point: Vertices = None):
    if start_point is None:
        for x in graph:

            for y in graph:
                y.visited = False

            res = is_cycle(graph, x, x)

            if res:
                return res
    else:
        for x in graph:

            if x.start_edge == point.destination_edge and x.visited is False:
                x.visited = True
                if point.destination_edge == start_point.start_edge:
                    return True
                res1 = is_cycle(graph, start_point, x)
                if res1:
                    return res1
    return False
