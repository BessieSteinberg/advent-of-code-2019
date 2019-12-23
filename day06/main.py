class Planet:
    def __init__(self, name):
        self.name = name
        self.orbit_parent = None
        self.num_orbits = 0
        self.children = []

    def set_orbit_parent(self, parent_planet):
        """
        Sets parent_planet as this planets orbit_planet
        Args:
            parent_planet: (Planet) orbit parent
        """
        self.orbit_parent = parent_planet
        parent_planet.add_child(self)
        parent_planet.update_child_orbits()

    def add_child(self, other_planet):
        """
        Adds other_planet to this planet's list of children
        Args:
            other_planet: (Planet) child planet
        """
        self.children.append(other_planet)

    def update_child_orbits(self):
        """
        Loops through this planet's children and updates their num_orbits values
        """
        for child in self.children:
            child.num_orbits = self.num_orbits + 1
            child.update_child_orbits()

    def __str__(self):

        if self.orbit_parent == None:
            return self.name

        return str(self.orbit_parent) + ' ) ' + self.name


class OrbitGraph:
    def __init__(self, orbit_map_file):
        """
        Args:
            orbit_map_file: (file)  File in the following format. Each line is read orbitee)orbiter
                COM)AA
                COM)XY
                AA)AB
                AA)BC
                XY)DE
                ...
        """
        self.planet_directory = {}

        with open(orbit_map_file) as orbit_map:
            line = orbit_map.readline()
            while line:
                planets = line.strip().split(')')
                orbitee = planets[0]
                orbiter = planets[1]

                # Check if each of these planets are in the directory, if they are not add them
                if not self.planet_directory.get(orbitee):
                    self.planet_directory[orbitee] = Planet(orbitee)

                if not self.planet_directory.get(orbiter):
                    self.planet_directory[orbiter] = Planet(orbiter)

                # Set orbitee as orbiter's parent
                self.planet_directory[orbiter].set_orbit_parent(self.planet_directory[orbitee])

                line = orbit_map.readline()

    def num_orbits(self):
        """
        Calculate the total number of orbits for all planets in this system
        Returns:
            (int) total number of direct and indirect orbits
        """
        sum_orbits = 0
        for planet in self.planet_directory.values():
            sum_orbits += planet.num_orbits

        return sum_orbits
