from argparse import ArgumentParser
from franky import Affine, CartesianMotion, Robot, ReferenceType, JointMotion, Gripper
import time

# Gripper parameters (global or pass as args)
GRASP_WIDTH = 0.03
GRASP_SPEED = 0.02
GRASP_FORCE = 20.0
EPSILON_OUTER = 0.01

def pick(robot, gripper):
    print("[INFO] Approaching object.")
    robot.move(CartesianMotion(Affine([0.0, 0.0, 0.2]), ReferenceType.Relative))
    time.sleep(1)

    print("[INFO] Gripping object.")
    gripper.grasp(GRASP_WIDTH, GRASP_SPEED, GRASP_FORCE, epsilon_outer=EPSILON_OUTER)
    time.sleep(1)

    print("[INFO] Lifting object.")
    robot.move(CartesianMotion(Affine([0.0, 0.0, -0.2]), ReferenceType.Relative))
    time.sleep(1)

def place(robot, gripper, y_offset):
    print(f"[INFO] Moving to drop location Y = {y_offset:.2f}.")
    robot.move(CartesianMotion(Affine([0.0, y_offset, 0.0]), ReferenceType.Relative))
    time.sleep(1)

    print("[INFO] Lowering object.")
    robot.move(CartesianMotion(Affine([0.0, 0.0, 0.2]), ReferenceType.Relative))
    time.sleep(1)

    print("[INFO] Releasing object.")
    gripper.open(GRASP_SPEED)
    time.sleep(1)

    print("[INFO] Lifting after drop.")
    robot.move(CartesianMotion(Affine([0.0, 0.0, -0.2]), ReferenceType.Relative))
    time.sleep(1)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--host", default="10.150.5.51", help="FCI IP of the robot")
    args = parser.parse_args()

    robot = Robot(args.host)
    gripper = Gripper(args.host)

    robot.recover_from_errors()
    robot.relative_dynamics_factor = 0.05

    print("[INFO] Moving to home joint pose.")
    robot.move(JointMotion([0.0, 0.0, 0.0, -2.2, 0.0, 2.2, 0.7]))
    time.sleep(1)

    # First pick and place (to Y = +0.2)
    pick(robot, gripper)
    place(robot, gripper, y_offset=0.2)

    # Second pick and place (to Y = -0.2)
    pick(robot, gripper)
    place(robot, gripper, y_offset=-0.2)

    print("[INFO] Returning to home joint pose.")
    robot.move(JointMotion([0.0, 0.0, 0.0, -2.2, 0.0, 2.2, 0.7]))
    time.sleep(1)

    print("[DONE] Pick-and-place routine complete.")
