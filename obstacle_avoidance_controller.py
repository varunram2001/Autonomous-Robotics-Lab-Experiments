"""obstacle_avoidance_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot


# get the time step of the current world.
TIMESTEP = 32
MAX_SPEED = 6.28


def run_robot(robot):
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  motor = robot.getDevice('motorname')
    #  ds = robot.getDevice('dsname')
    #  ds.enable(timestep)
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    list_ps = []
    for ind in range(0,8):
        sensor_name = 'ps'+str(ind)
        list_ps.append(robot.getDevice(sensor_name))
        list_ps[-1].enable(TIMESTEP)
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(TIMESTEP) != -1:
        left_speed = MAX_SPEED
        right_speed = MAX_SPEED
        # Read the sensors:
        # Enter here functions to read sensor data, like:
        #  val = ds.getValue()
        for ps in list_ps:
            ps_val = ps.getValue()
            print(ps_val)
            if ps_val>100:
                left_speed = -MAX_SPEED
                
                
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
        # Process sensor data here.
    
        # Enter here functions to send actuator commands, like:
        #  motor.setPosition(10.0)
        pass

# Enter here exit cleanup code.

if __name__ == "__main__":
    robot = Robot()
    run_robot(robot)