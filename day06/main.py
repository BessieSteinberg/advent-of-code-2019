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

    def most_recent_shared_ancestor(self, other_planet):
        """
        Finds the most recent shared ancestor of this planet and other_planet
        Args:
            other_planet: (Planet)

        Returns:
            shared_ancestor (Planet)
        """
        ancestors = set()
        current_ancestor = self.orbit_parent
        while current_ancestor is not None:
            ancestors.add(current_ancestor)
            current_ancestor = current_ancestor.orbit_parent

        # Find most recent ancestor of other_planet that is in the ancestors set
        current_ancestor = other_planet.orbit_parent
        while current_ancestor is not None:
            if current_ancestor in ancestors:
                return current_ancestor

            current_ancestor = current_ancestor.orbit_parent

        return None

    def min_orbit_transfers(self, other_planet):
        """
        Calculates the minimum orbital transfers required between this and the other planet
        Args:
            other_planet: (Planet)

        Returns:
            (int) number of orbital transfers
        """
        shared_ancestor = self.most_recent_shared_ancestor(other_planet)

        # Calculate the distance from the other planet to the shared ancestor
        dist_other_planet = 0
        current_planet = other_planet.orbit_parent
        while current_planet is not shared_ancestor:
            current_planet = current_planet.orbit_parent
            dist_other_planet += 1

        # Calculate the distance from this planet to the shared ancestor
        dist_this_planet = 0
        current_planet = self.orbit_parent
        while current_planet is not shared_ancestor:
            current_planet = current_planet.orbit_parent
            dist_this_planet += 1

        return dist_other_planet + dist_this_planet

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

    def most_recent_shared_ancestor(self, planet1, planet2):
        """
        Returns the most recent shared ancestor between these two planets
        Args:
            planet1: (str) Planet representation
            planet2: (str) Planet representation

        Returns:
            (str) planet representation
        """
        planet1 = self.planet_directory[planet1]
        planet2 = self.planet_directory[planet2]

        shared_ancestor = planet1.most_recent_shared_ancestor(planet2)

        return shared_ancestor.name

    def min_orbit_transfers(self, planet1, planet2):
        """
        Returns the min number of orbit transfers between these two planets
        Args:
            planet1: (str) Planet representation
            planet2: (str) Planet representation

        Returns:
            (int) orbit transfers
        """
        planet1 = self.planet_directory[planet1]
        planet2 = self.planet_directory[planet2]

        return planet1.min_orbit_transfers(planet2)
