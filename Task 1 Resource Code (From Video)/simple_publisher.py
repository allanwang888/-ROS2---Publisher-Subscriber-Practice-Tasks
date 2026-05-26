
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher_node")

        self.publisher = self.create_publisher(String, "robot_news", 10)

        self.timer = self.create_timer(1.0, self.timer_callback)

        self.i = 0

    def timer_callback(self):
        message = String()

        message.data = f"Hello, how are you? [ Message Number ]: {self.i}"

        self.publisher.publish(message)
        
        self.get_logger().info(f"Publishing: {message.data}")
        
        self.i += 1


def main(args = None):
    rclpy.init(args = args)

    node = SimplePublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()



if __name__ == "__main__":
    main()

