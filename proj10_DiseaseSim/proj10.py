# proj10: Simulating the Spread of Disease and Virus Population Dynamics
# Name:
# Date:

# import numpy
import random
# import pylab


''' 
Begin helper code
'''


class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """


'''
End helper code
'''


#
# PROBLEM 1
#
class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """

    def __init__(self, maxBirthProb, clearProb):
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        # TODO

    def doesClear(self):
        if random.random() < self.clearProb:
            return True
        else:
            return False


        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.clearProb and otherwise returns
        False.
        """

        # TODO

    def reproduce(self, popDensity):
        if random.random() < self.maxBirthProb * (1-popDensity):
            x = True
        else:
            x = False
        if x:
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        # TODO


class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        self.viruses = viruses
        self.maxPop = maxPop
        """

        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """

        # TODO

    def getTotalPop(self):
        return len(self.viruses)
        # """
        # Gets the current total virus population.
        # returns: The total virus population (an integer)
        # """

        # TODO

    def update(self):
        for item in self.viruses:
            if item.doesClear():
                self.viruses.remove(item)
            else:
                x = self.getTotalPop() / self.maxPop
                try:
                    self.viruses.append(item.reproduce(x))

                except NoChildException:
                    continue
        return self.getTotalPop()








        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """

        # TODO


#
# PROBLEM 2
#
def simulationWithoutDrug():
    lst = []
    lst2 = []
    lst3 = []
    counter = 1
    for i in range(1, 101):
        lst.append(SimpleVirus(0.1, 0.05))
    patient = SimplePatient(lst, 1000)
    for i in range(1, 301):
        lst2.append(patient.update())
        lst3.append(counter)
        counter = counter + 1
    print lst2
    print lst3



    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """

    # TODO
simulationWithoutDrug()