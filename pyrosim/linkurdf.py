from pyrosim.originurdf      import ORIGIN_URDF

from pyrosim.geometryurdf    import GEOMETRY_URDF

from pyrosim.inertialurdf    import INERTIAL_URDF

from pyrosim.visualurdf      import VISUAL_URDF

from pyrosim.collisionurdf   import COLLISION_URDF

from pyrosim.commonFunctions import Save_Whitespace

from pyrosim.material        import MATERIAL

class LINK_URDF:

    def __init__(self,name,pos,size,color,colorname):

        self.name = name

        self.depth = 1

        self.origin   = ORIGIN_URDF(pos)

        self.inertial  = INERTIAL_URDF(self.origin)

        self.geometry = GEOMETRY_URDF(size)

        self.material = MATERIAL(color,name)

        self.visual    = VISUAL_URDF(self.origin , self.geometry, color, colorname)

        self.collision = COLLISION_URDF(self.origin , self.geometry)

    def Save(self,f):

        self.Save_Start_Tag(f)

        self.inertial.Save(f)

        self.visual.Save(f)

        self.collision.Save(f)

        self.Save_End_Tag(f)

# ------------------- Private methods -----------------

    def Save_End_Tag(self,f):

        Save_Whitespace(self.depth,f)

        f.write('</link>\n')

    def Save_Start_Tag(self,f):

        Save_Whitespace(self.depth,f)

        f.write('<link name="' + self.name + '">\n')
