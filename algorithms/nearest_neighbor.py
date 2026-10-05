def nearest_neighbor(points, start=0):
    unvisited = set(range(len(points)))
    path = [start]
    unvisited.remove(start)
    while unvisited:
        last = path[-1]
        nxt = min(unvisited,
                  key=lambda i: (points[i][0]-points[last][0])**2 +
                                (points[i][1]-points[last][1])**2)
        path.append(nxt); unvisited.remove(nxt)
    return path
