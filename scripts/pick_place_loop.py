from argparse import ArgumentParser
from franky import Affine, CartesianMotion, Robot, ReferenceType, JointMotion, Gripper
import time

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--host", default="10.150.5.51", help="FCI IP of the robot")
    args = parser.parse_args()

    # Connect to the robot arm and gripper
    robot = Robot(args.host)
    gripper = Gripper(args.host)

    # Recover and set safe dynamics
    robot.recover_from_errors()
    robot.relative_dynamics_factor = 0.05

    # Gripper parameters
    grasp_width = 0.03        # 3 cm
    grasp_speed = 0.02        # 2 cm/s
    grasp_force = 20.0        # Newtons
    epsilon_outer = 0.01      # Acceptable tolerance

    print("[INFO] Moving to home joint pose.")
    robot.move(JointMotion([0.0, 0.0, 0.0, -2.2, 0.0, 2.2, 0.7]))
    time.sleep(1)

    print("[INFO] Approaching first object.")
    robot.move(CartesianMotion(Affine([0.0, 0.0, 0.2]), ReferenceType.Relative))
    time.sleep(1)

    print("[INFO] Gripping first object.")
    gripper.grasp(grasp_width, grasp_speed, grasp_force, epsilon_outer=epsilon_outer)
    time.sleep(1)

    print("[INFO] Lifting first object.")
    robot.move(CartesianMotion(Affine([0.0, 0.0, -0.2]), ReferenceType.Relative))
    time.sleep(1)

    print("[INFO] Moving to drop location Y = +0.2.")
    robot.move(CartesianMotion(Affine([0.0, 0.2, 0.0]), ReferenceType.Relative))
    time.sleep(1)

    print("[INFO] Lowering for drop.")
    robot.move(CartesianMotion(Affine([0.0, 0.0, 0.2]), ReferenceType.Relative))
    time.sleep(1)

    print("[INFO] Releasing object.")
    gripper.open(grasp_speed)
    time.sleep(1)

    print("[INFO] Lifting after drop.")
    robot.move(CartesianMotion(Affine([0.0, 0.0, -0.2]), ReferenceType.Relative))
    time.sleep(1)

    print("[INFO] Approaching second object.")
    robot.move(CartesianMotion(Affine([0.0, 0.0, 0.2]), ReferenceType.Relative))
    time.sleep(1)

    print("[INFO] Gripping second object.")
    gripper.grasp(grasp_width, grasp_speed, grasp_force, epsilon_outer=epsilon_outer)
    time.sleep(1)

    print("[INFO] Lifting second object.")
    robot.move(CartesianMotion(Affine([0.0, 0.0, -0.2]), ReferenceType.Relative))
    time.sleep(1)

    print("[INFO] Moving to drop location Y = -0.2.")
    robot.move(CartesianMotion(Affine([0.0, -0.2, 0.0]), ReferenceType.Relative))
    time.sleep(1)

    print("[INFO] Lowering for second drop.")
    robot.move(CartesianMotion(Affine([0.0, 0.0, 0.2]), ReferenceType.Relative))
    time.sleep(1)

    print("[INFO] Releasing second object.")
    gripper.open(grasp_speed)
    time.sleep(1)

    print("[INFO] Returning to home joint pose.")
    robot.move(JointMotion([0.0, 0.0, 0.0, -2.2, 0.0, 2.2, 0.7]))
    time.sleep(1)

    print("[DONE] Pick-and-place routine complete.")
