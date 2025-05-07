from franky import *

robot = Robot("10.150.5.51")  # Replace with your robot's IP
robot.relative_dynamics_factor = 0.05

motion = CartesianMotion(Affine([0.2, 0.0, 0.0]), ReferenceType.Relative)
robot.move(motion)
