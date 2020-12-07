# Creds: @sorensenmarius on Github

import numpy as np

route = open('route.txt', 'r').read()

moves = {'O': [-1, 0], 'H': [0, 1], 'N': [1, 0], 'V': [0, -1]}
edges = [(0, 0)]
for move in route:
    edges.append(np.add(edges[-1], moves[move]))

area = 0.5 * abs(sum(x0 * y1 - x1 * y0 for ((x0, y0), (x1, y1)) in zip(edges, edges[1:] + [edges[0]])))
print(f'Area: {int(area)}')
