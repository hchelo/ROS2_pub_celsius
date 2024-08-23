# ROS2_pub_celsius
--Hacer un programa que:
--Implemente un nodo publicador que publique la temperatura en grados Celsius en un tópico llamado /temperature_celsius a una frecuencia de 1 Hz.
--Implemente un nodo suscriptor que se suscriba a este tópico, convierta la temperatura a grados Fahrenheit y publique el resultado en un nuevo tópico llamado /temperature_fahrenheit.

# Crear el paquete en un src
    ros2 pkg create --build-type ament_python fahrenheit
# Escribir Nodo 1
	  pub_temp_celsius.py
# Escribir Nodo 2
    sus_pub_temp_fahrenheit.py
# Escribir Nodo 3
    sus_nuevo.py
# Agregar dependencias al package.xml
    <exec_depend>rclpy</exec_depend>
    <exec_depend>std_msgs</exec_depend>
# Añadir punto de entrada en setup.py
        entry_points={
        'console_scripts': [
        	'talker2 = fahrenheit.pub_temp_celsius:main',
        	'listener2 = fahrenheit.sus_pub_temp_fahrenheit:main',
        	'talker3 = fahrenheit.sus_pub_temp_fahrenheit:main',
        	'listener3 = fahrenheit.sus_nuevo:main',
          ],
        },
# Construir y ejecutar
    colcon build --packages-select fahrenheit
	  source install/setup.bash
- Terminal 1
   * ros2 run fahrenheit talker2
- Terminal 2
  * ros2 run fahrenheit listener2
- Terminal 3    
  * ros2 run fahrenheit listener3
