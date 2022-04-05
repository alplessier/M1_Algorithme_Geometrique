import halfedge_mesh

# .off are supported
mesh = halfedge_mesh.HalfedgeMesh("tests/data/mesh02.off")

# Returns a list of Vertex type (in order of file)--similarly for halfedges,
# and facets
mesh.vertices

# The number of facets in the mesh
len(mesh.facets)

# Get the 10th halfedge
mesh.halfedges[10]

# Get the halfedge that starts at vertex 25 and ends at vertex 50
# will not work with a random mesh
# mesh.get_halfedge(25, 50)

# Iterate over the vertices of the mesh
mesh.save_vertices("tests/data/cube2.off")

#print(mesh.get_distances(0))

i = mesh.parcoursGraph()
print(i)
print(mesh.calculX(i))