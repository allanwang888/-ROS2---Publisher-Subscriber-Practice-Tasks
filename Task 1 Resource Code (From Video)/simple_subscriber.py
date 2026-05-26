
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimpleSubscriber(Node):
    def __init__(self):
        super().__init__("simple_subscriber_node")

        self.subscription = self.create_subscription(String, "robot_news", self.listener_callback, 10)

    def listener_callback(self, message_from_publisher):
        self.get_logger().info(f"I received this: '{message_from_publisher.data}'")


def main(args = None):
    rclpy.init(args = args)

    node = SimpleSubscriber()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
