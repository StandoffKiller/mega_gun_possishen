import pymesh as ph

class ob():

    def __init__(self, screen):
        array = []
        self.screen = screen
        mesh = ph("IronMan.obj")
        array([[-1., -1., 1.],
               ...
               [1., 1., 1.]])
        type(mesh.vertices)
        mesh.add_attribute("vertex_gaussian_curvature");
        mesh.get_attribute("vertex_gaussian_curvature");
        array([1.57079633, 1.57079633, 1.57079633, 1.57079633, 1.57079633,
               1.57079633, 1.57079633, 1.57079633])
    def output(self):
        "рисование пушки"
        self.screen.blit(self.image, self.rect)
