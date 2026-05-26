import rclpy

from rclpy.node import Node

from std_msgs.msg import String


class SatelliteTelemetry(Node):

    def __init__(self):

        super().__init__('satellite_telemetry_node')

        self.publisher_ = self.create_publisher(String, 'satellite_data', 10)

        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):

        msg = String()

        msg.data = 'Speed: 27000 km/h, Altitude: 420 km'

        self.publisher_.publish(msg)

        self.get_logger().info(f'Publishing: "{msg.data}"')


def main(args=None):

    rclpy.init(args=args)

    node = SatelliteTelemetry()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()




if __name__ == '__main__':

    main()







