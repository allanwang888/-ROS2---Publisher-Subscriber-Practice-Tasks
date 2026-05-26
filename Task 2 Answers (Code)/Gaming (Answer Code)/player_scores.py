import rclpy

from rclpy.node import Node

from std_msgs.msg import String


class PlayerScores(Node):

    def __init__(self):

        super().__init__('player_scores_node')

        self.publisher_ = self.create_publisher(String, 'game_scores', 10)

        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):

        msg = String()

        msg.data = 'Player1 Score: 9500 HP: 100'

        self.publisher_.publish(msg)

        self.get_logger().info(f'Publishing: "{msg.data}"')


def main(args=None):

    rclpy.init(args=args)

    node = PlayerScores()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()




if __name__ == '__main__':

    main()

