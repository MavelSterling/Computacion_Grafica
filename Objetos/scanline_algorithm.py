import matplotlib.pyplot as plt

def scanline_algorithm(vertices):
    min_y = min(vertices, key=lambda vertex: vertex[1])[1]
    max_y = max(vertices, key=lambda vertex: vertex[1])[1]
    
    active_edges = []
    intersections = []
    for y in range(min_y, max_y + 1):
        for i in range(len(vertices)):
            vertex1 = vertices[i]
            vertex2 = vertices[(i + 1) % len(vertices)]
            if vertex1[1] < y and vertex2[1] >= y or vertex2[1] < y and vertex1[1] >= y:
                edge = (vertex1, vertex2)
                active_edges.append(edge)
        
        active_edges = [edge for edge in active_edges if edge[1][1] != y]
        
        intersections.clear()
        for edge in active_edges:
            x = edge[0][0] + (y - edge[0][1]) * (edge[1][0] - edge[0][0]) / (edge[1][1] - edge[0][1])
            intersections.append(x)
        
        intersections.sort()
        for i in range(0, len(intersections), 2):
            plt.plot([intersections[i], intersections[i+1]], [y, y], color='black')

# Definir los vértices del polígono
vertices = [
    (2, 1),
    (4, 6),
    (7, 3),
    (5, 1)
]

# Aplicar el algoritmo de línea de exploración
scanline_algorithm(vertices)

# Configurar el gráfico
plt.axis('equal')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Algoritmo de Línea de Exploración')

# Mostrar el gráfico resultante
plt.show()
