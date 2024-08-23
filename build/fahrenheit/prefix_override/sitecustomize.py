import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/kubu/ROS2/pub_far_cel_ws/install/fahrenheit'
