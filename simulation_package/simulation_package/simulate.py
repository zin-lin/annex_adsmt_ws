import gym
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from ros_gz_interfaces.msg import WorldReset
from gz.transport13 import Node as IgnitionNode


class QuadrupedEnv(gym.Env):
    def __init__(self):
        super(QuadrupedEnv, self).__init__()

        # Initialize ROS 2 node
        rclpy.init()
        self.node = rclpy.create_node("quadruped_env")

        # Action space: 12 values for 12 joints (range from -1 to 1)
        self.action_space = gym.spaces.Box(low=-1.0, high=1.0, shape=(12,), dtype=np.float32)

        # Observation space: 24 values (12 joint positions + 12 joint velocities)
        self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(24,), dtype=np.float32)

        # ROS 2 Publishers for each joint (assuming standard Float64 messages)
        self.joint_publishers = [
            self.node.create_publisher(Float64, f"/quadruped/joint{i}_controller/command", 10)
            for i in range(12)
        ]

        # ROS 2 Subscriber to get joint states
        self.joint_states = np.zeros(12)
        self.node.create_subscription(JointState, "/quadruped/joint_states", self.joint_state_callback, 10)

        # Ignition Transport Node for simulation_package reset
        self.ign_node = IgnitionNode()
        # Publisher for WorldReset message
        self.reset_pub = self.node.create_publisher(WorldReset, "/world/default/control/reset", 10)

        self.reset()

    def joint_state_callback(self, msg):
        """Update joint states (position and velocity)."""
        self.joint_states = np.array(msg.position[:12])  # First 12 values represent positions

    def step(self, action):
        """Apply joint actions and return new state, reward, and done flag."""
        for i in range(12):
            msg = Float64()
            msg.data = action[i]
            self.joint_publishers[i].publish(msg)  # Send joint command

        rclpy.spin_once(self.node, timeout_sec=0.1)

        # Observation is just the current joint states (position/velocity)
        obs = self.joint_states

        # Reward function: distance covered by the robot, should be adjusted
        reward = self.calculate_reward()

        done = False  # Set condition for when the robot "fails"
        return obs, reward, done, {}

    def calculate_reward(self):
        """Reward function for walking cycle, can be refined."""
        # Reward based on distance traveled by the robot, leg coordination, etc.
        forward_movement = np.sum(self.joint_states[:12])  # Example metric
        return forward_movement

    def reset(self,*, seed=None, return_info=False, options=None):
        """Reset the simulation_package using a reset publisher."""
        """Reset the simulation_package using the correct WorldReset message."""
        reset_msg = WorldReset()
        reset_msg.all = True  # Reset everything in the world
        self.reset_pub.publish(reset_msg)

        rclpy.spin_once(self.node, timeout_sec=1)
        return np.zeros(24)  # Reset to zero state

    def render(self, mode="human"):
        pass

    def close(self):
        self.node.destroy_node()
        rclpy.shutdown()
