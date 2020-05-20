import numpy as np

class Atom:
    """Class representing a chmeical atom. Each atom has coordinates (x,y,z) and a name."""
    
    def __init__(self, name, coords):
        """returns new atom.Atom object"""
        self.name, self.coords = name, coords
    
    def copy(self):
        """Method that returns a deep copy of the current atom"""
        coords = np.copy(self.coords)
        return Atom(self.name, coords)

    def move(self, p):
        """Method that moves the atom by a specified 1x3 [X,Y,Z] list of floats"""
        self.coords += p
    
    def to_pdb_str(self, acount=1):
        """Creates a string representation of the atom that is compatible with the PDB format"""
        if self == None:
            raise TypeError

        return  "ATOM {:6d}  P   C   A   1 {:11.3f}{:8.3f}{:8.3f}  1.00 62.18           P\n".format(
                acount,
                self.coords[0],
                self.coords[1],
                self.coords[2])

    def __str__(self):
        """Returns the string representation of the object with the format NAME X Y Z"""
        return self.name + " " + ' '.join([str(val) for val in self.coords])


    def __repr__(self):
        """Returns the string representation of the object with the format NAME X Y Z. Used for debugging purposes only"""
        return str(self)
