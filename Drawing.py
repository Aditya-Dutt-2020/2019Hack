import anki_vector
import time

with anki_vector.Robot() as robot:
    robot.motors.set_wheel_motors(-50,50)
    time.sleep(4.0)
