import anki_vector
import time
with anki_vector.Robot() as robot:
    robot.motors.set_lift_motor(-5.0)
    time.sleep(0.2)
    robot.motors.set_lift_motor(5.0)
    time.sleep(0.2)

    args = anki_vector.util.parse_command_args()
with anki_vector.Robot(args.serial) as robot:
    print("Everybody clap your hands""clap clap clap clap clap")
    robot.behavior.say_text("Everybody clap your hands""clap clap clap clap clap")

with anki_vector.Robot() as robot:
    robot.motors.set_wheel_motors(-100,100)
    time.sleep(.25)
    with anki_vector.Robot(args.serial) as robot:
        print ("To the left")
        robot.behavior.say_text("To the left")

with anki_vector.Robot() as robot:
    robot.motors.set_wheel_motors(-100,-100)
    time.sleep(.1)
    with anki_vector.Robot(args.serial) as robot:
        print("take it back now y'all")
        robot.behavior.say_text("take it back now y'all, chah chah real smooth")
    robot.motors.set_wheel_motor(100,100)
    time.sleep(.1)

with anki_vector.Robot() as robot:
    with anki_vector.Robot(args.serial) as robot:
        print("Cha Cha real smooth")
        robot.behavior.say_text("Cha Cha real smooth")
    robot.motors.set_wheel_motors(-100,100)
    time.sleep(.1)
