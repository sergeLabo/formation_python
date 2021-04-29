
# Construire un Message à envoyé en OSC

# il y a toujours 8 points dans points: len(points) = 8
points = [[0, 0], [-1.56,  -2.78], [0, 1.2],  [1.2, 0], [45, 54], [10, 10],
          [45, 78], None, None]

# Si None --> -1000, -1000
# Consruire le msg
# msg = [0, 0, -1.56, ....., -1000, -1000]

msg = []
for point in points:
    if point:
