import rclpy

from rclpy.node import Node

from std_msgs.msg import String


class TemperatureSensor(Node):

    def __init__(self):

        super().__init__('temperature_sensor_node')

        self.publisher_ = self.create_publisher(String, 'home_temp', 10)

        self.timer = self.create_timer(2.0, self.timer_callback)

    def timer_callback(self):

        msg = String()

        msg.data = 'Current Living Room Temperature: 21.5C'

        self.publisher_.publish(msg)

        self.get_logger().info(f'Publishing: "{msg.data}"')


def main(args=None):

    rclpy.init(args=args)

    node = TemperatureSensor()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()




if __name__ == '__main__':

    main()
