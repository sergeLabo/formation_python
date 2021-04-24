
# Construire un Message à envoyé en OSC

points = [[0, 0], [-1.56,  -2.78], [0, 1.2],  [1.2, 0], [45, 54], [10, 10],
          [45, 78], None, None]

# Si None --> -1000, -1000
# Consruire le msg
# msg = [0, 0, -1.56, ....., -1000, -1000]

for point in points:
    if point:
