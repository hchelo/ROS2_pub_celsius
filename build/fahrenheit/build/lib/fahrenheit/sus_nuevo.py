import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TempFahrenheit2(Node):

    def __init__(self):
        super().__init__('temperature_fahrenheit2')
        self.subscription = self.create_subscription(
            String,
            'topic2',
            self.listener_callback,
            10)
        self.subscription  # evita que la variable de suscripción sea eliminada por el recolector de basura

    def listener_callback(self, msg):
        self.get_logger().info(f'{msg.data}')

def main(args=None):
    rclpy.init(args=args)

    temperature_fahrenheit2 = TempFahrenheit2()
    rclpy.spin(temperature_fahrenheit2)

    # Destruye el nodo explícitamente
    temperature_fahrenheit2.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
