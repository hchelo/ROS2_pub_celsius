import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TempCelsius(Node):

    def __init__(self):
        super().__init__('temp_celsius')
        self.publisher_ = self.create_publisher(String, 'topic1', 10)
        timer_period = 3
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello, ROS 2 123: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando msa: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    temp_celsius = TempCelsius()
    rclpy.spin(temp_celsius)
    # Destruye el nodo explícitamente
    temp_celsius.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
