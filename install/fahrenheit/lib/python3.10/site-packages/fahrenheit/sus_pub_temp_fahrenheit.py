import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TempFahrenheit(Node):

    def __init__(self):
        super().__init__('temperature_fahrenheit')
        self.subscription = self.create_subscription(
            String,'topic1',self.listener_callback,10)
        self.subscription  # evita que la variable de suscripción sea eliminada 
        # Crear un publicador para el nuevo tópico
        self.publisher_ = self.create_publisher(String, '/topic2', 10)

    def listener_callback(self, msg):
        # Mostrar el mensaje recibido
        self.get_logger().info(f'Recibido: "{msg.data}"')
        # Dividir la cadena por los dos puntos (:)
        parts = msg.data.split(':')
        # eliminar comillas
        message_part = parts[-1].strip()
        # Dividir por espacio y obtener el último elemento que es el número
        number_str = message_part.split()[-1]
        # Eliminar comillas y espacios adicionales
        number_str = number_str.replace('"', '').strip()
        # Convertir a entero
        try:
            celsius = int(number_str)
        except ValueError:
            self.get_logger().error(f'Error al convertir el número: {number_str}')
            return

        # Convertir Celsius a Fahrenheit
        fahrenheit = (celsius * 9/5) + 32
        # Convertir el resultado a cadena
        fahrenheit_str = str(fahrenheit)
        # Mostrar el número en Celsius y Fahrenheit
        self.get_logger().info(f'Temperatura en Celsius: {celsius}')
        self.get_logger().info(f'Temperatura en Fahrenheit: {fahrenheit_str}')
        # Crear y publicar el mensaje en el nuevo tópico
        fahrenheit_msg = String()
        fahrenheit_msg.data = fahrenheit_str
        self.publisher_.publish(fahrenheit_msg)
        self.get_logger().info(f'Publicado en /temperature_fahrenheit: "{fahrenheit_str}"')

def main(args=None):
    rclpy.init(args=args)
    temperature_fahrenheit = TempFahrenheit()
    rclpy.spin(temperature_fahrenheit)  
    # Destruye el nodo explícitamente
    temperature_fahrenheit.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
