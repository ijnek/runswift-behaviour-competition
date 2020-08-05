import robot


def walk(forward, left, turn):
    return robot.BodyCommand(
        robot.ActionType.WALK, int(forward), int(left), float(turn),  # specify some parameters
        1, 1, 1, robot.Foot.LEFT, False, False, False, False, False)  # you don't have to know what these parameters are


def tick(blackboard):
    request = robot.BehaviourRequest()
    request.actions.body = walk(100, 100, 0)

    return request