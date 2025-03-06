import rclpy
from rclpy.node import Node
from annex_msgs.msg import Vcu2ai, Ai2vcu
from sensor_msgs.msg import JointState


JOINTS = ['joint_1', 'joint_1_1','joint_1_1_1', 'joint_2','joint_2_1', 'joint_2_1_1',
'joint_3', 'joint_3_1','joint_3_1_1', 'joint_4','joint_4_1', 'joint_4_1_1'
          ]

class SimNode(Node):
    def __init__(self):
        super().__init__('simulation_simple_node')

        # create timer
        self.timer = self.create_timer(0.1, self.timer_callback, )

        # create publisher
        self.publish_robotics = self.create_publisher(JointState,'/joint_states', 10)

    def timer_callback(self):
        msg = JointState()
        msg.name = JOINTS
        msg.position = [3.0,3.0,3.0,3.0,3.0,3.0,3.0,3.0,3.0,3.0,3.0,3.0]

        self.publish_robotics.publish(msg)

# main method
def main(args=None):
    rclpy.init(args=args)

    sim_node = SimNode()

    rclpy.spin(sim_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    sim_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


