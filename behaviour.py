import robot

bb = None  # Global blackboard variable
request = None  # Global request variable

# Function to make robot walk
def walk(forward, left, turn):  # mm/s, mm/s, rad/s
    global request
    request = robot.BehaviourRequest()
    request.actions.body = robot.BodyCommand(
          robot.ActionType.WALK, int(forward), int(left), float(turn),  # specify some parameters
          1, 1, 1, robot.Foot.LEFT, False, False, False, False, False)  # you don't have to know what these parameters are

# Ball's relative x position in robot's cartesian coordinates
def ballRelPosX():
    return bb.stateEstimation.ballPosRRC.x

# Ball's relative y position in robot's cartesian coordinates
def ballRelPosY():
    return bb.stateEstimation.ballPosRRC.y


def tick(blackboard):
    # Update bb variable with new blackboard
    global bb
    bb = blackboard

    ##### YOUR CODE GOES BELOW HERE #####

    walk(100, 100, 0) # Walk 100mm/s forwards and 100mm/s left

    ##### YOUR CODE GOES ABOVE HERE ######

    # Check whether the request was set
    if (request is None):
        print("YOU MUST REQUEST AN ACTION BY CALLING WALK")
    return request