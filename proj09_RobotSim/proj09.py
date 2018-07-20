# proj09: Simulating robots
# Name:
# Date:

import math
import random
import proj09_visualize

# import pylab


# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

# === Problems 1

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = width * height
        self.cleantiles = []


        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """

    
    def cleanTileAtPosition(self, pos):
        x = int(pos.getX())
        y = int(pos.getY())
        if [x, y] not in self.cleantiles:
            self.cleantiles.append([x, y])




        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """


    def isTileCleaned(self, m, n):

        for l in self.cleantiles:
            if l[0] == m and l[1] == n:
                return True
        return False



    
    def getNumTiles(self):
        return self.tiles


    def getNumCleanedTiles(self):

        return len(self.cleantiles)
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """


    def getRandomPosition(self):

        x = random.randint(0, self.width)
        y = random.randint(0, self.height)
        return Position(x, y)
        """
        Return a random position inside the room.

        returns: a Position object.
        """


    def isPositionInRoom(self, pos):
        x = pos.getX()
        y = pos.getY()
        if x < 0 or x > self.width:
            return False
        if y < 0 or y > self.height:
            return False
        return True

        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """



class Robot(object):



    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """

    
    def __init__(self, room, speed):

        self.speed = speed
        self.room = room
        self.direction = random.randint(0, 360)
        self.position = room.getRandomPosition()

        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """


    def getRobotPosition(self):
        x = self.position.getX()
        y = self.position.getY()
        return Position(x, y)




    
    def getRobotDirection(self):

        return self.direction

        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """


    def setRobotPosition(self, position):

        x = position.getX()
        y = position.getY()
        self.position = Position(x, y)

        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """


    def setRobotDirection(self, d):

        if 0 <= d < 360:
            self.direction = d
        elif d > 360:
            while d > 360:
                d -= 360
            self.direction = d
        elif d < 0:
            while d < 0:
                d += 360
            self.direction = d


        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """


    def updatePositionAndClean(self):

        self.position = self.position.getNewPosition()
        self.room.cleanTileAtPosition(self.position)

        raise NotImplementedError

        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """



# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):

        pos = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(pos) is True:
            Robot.setRobotPosition(self, pos)
            self.room.cleanTileAtPosition(self.position)
        if self.room.isPositionInRoom(pos) is False:
            d = random.randint(0,360)
            Robot.setRobotDirection(self, d)
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    ta = 0
    nt = num_trials
    while nt > 0:
        anim = proj09_visualize.RobotVisualization(num_robots, width, height)
        robots = []
        avgt = 0
        room = RectangularRoom(width, height)
        for k in range(0, num_robots):
            robots.append(robot_type(room, speed))
        timestep = 0
        while int(room.getNumTiles() * min_coverage) - 1 >= room.getNumCleanedTiles():
            for robot in robots:
                robot.updatePositionAndClean()
            anim.update(room, robots)
            timestep += 1
        avgt += timestep
        ta += avgt
        nt -= 1
    trials = float(ta) / float(num_trials)
    print trials
    anim.done()
    return trials


    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    raise NotImplementedError


# === Problem 4
#
# 1) How long does it take to clean 80% of a 20x20 room with each of 1-10 robots?
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions 
#	 20x20, 25x16, 40x10, 50x8, 80x5, and 100x4?

def showPlot1():

    times = []
    for num_robots in range(1, 11):
        times.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 30, StandardRobot))
    print times

    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """ 
    raise NotImplementedError

def showPlot2():

    xdim_lst = [20, 25, 40, 50, 80, 100]
    ydim_lst = [20, 16, 10, 8, 5, 4]
    for item in xdim_lst:
        for i in ydim_lst:
            avg = runSimulation(2, 1.0, item, i, 0.8, 30, StandardRobot)
    print avg

    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    raise NotImplementedError

# === Problem 5

class RandomWalkRobot(Robot):

    def updatePositionAndClean(self):
        d = random.randint(0, 360)
        Robot.setRobotDirection(self, d)
        pos = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(pos) is True:
            Robot.setRobotPosition(self, pos)
            self.room.cleanTileAtPosition(self.position)

    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """



# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    raise NotImplementedError

print runSimulation(1, 1, 10, 10, 1.0, 1, RandomWalkRobot)