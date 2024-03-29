## *********************************************************
##
## File autogenerated for the roboteq_control package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 245, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 290, 'description': '[#] Gear ratio', 'max': inf, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'ratio', 'edit_method': '', 'default': 1.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 290, 'description': 'Versus of the rotation of the motor', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'rotation', 'edit_method': "{'enum_description': 'Rotation versus wheel', 'enum': [{'srcline': 10, 'description': 'Clockwise rotation', 'srcfile': '/home/zeged/catkin_ws/src/armadillo2/armadillo2_utils/roboteq_control/cfg/RoboteqParameter.cfg', 'cconsttype': 'const int', 'value': -1, 'ctype': 'int', 'type': 'int', 'name': 'Clockwise'}, {'srcline': 11, 'description': 'Counterclockwise rotation', 'srcfile': '/home/zeged/catkin_ws/src/armadillo2/armadillo2_utils/roboteq_control/cfg/RoboteqParameter.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Counterclockwise'}]}", 'default': 1, 'level': 0, 'min': -1, 'type': 'int'}, {'srcline': 290, 'description': 'Stall detection', 'max': 3, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'stall_detection', 'edit_method': "{'enum_description': 'Stall configuration', 'enum': [{'srcline': 15, 'description': 'Disabled', 'srcfile': '/home/zeged/catkin_ws/src/armadillo2/armadillo2_utils/roboteq_control/cfg/RoboteqParameter.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Disabled'}, {'srcline': 16, 'description': '250ms at 10% power', 'srcfile': '/home/zeged/catkin_ws/src/armadillo2/armadillo2_utils/roboteq_control/cfg/RoboteqParameter.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': '250ms_at_10percent'}, {'srcline': 17, 'description': '500ms at 25% power', 'srcfile': '/home/zeged/catkin_ws/src/armadillo2/armadillo2_utils/roboteq_control/cfg/RoboteqParameter.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': '500ms_at_25percent'}, {'srcline': 18, 'description': '1000ms at 50% power', 'srcfile': '/home/zeged/catkin_ws/src/armadillo2/armadillo2_utils/roboteq_control/cfg/RoboteqParameter.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': '1000ms_at_50percent'}]}", 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 290, 'description': '[A] Amper limit', 'max': 20.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'amper_limit', 'edit_method': '', 'default': 5.0, 'level': 0, 'min': 1.0, 'type': 'double'}, {'srcline': 290, 'description': '[%] IN MODULE - Maximum power forward', 'max': 100, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'max_forward', 'edit_method': '', 'default': 100, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 290, 'description': '[%] IN MODULE - Maximum power reverse', 'max': 100, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'max_reverse', 'edit_method': '', 'default': 100, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 290, 'description': '[RPM] max motor speed (after gear reduction)', 'max': inf, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'max_speed', 'edit_method': '', 'default': 10.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 290, 'description': '[RPM/s] max motor acceleration (after gear reduction)', 'max': inf, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'max_acceleration', 'edit_method': '', 'default': 1000.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 290, 'description': '[RPM/s] max motor deceleration (after gear reduction)', 'max': inf, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'max_deceleration', 'edit_method': '', 'default': 1000.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 290, 'description': 'Load all parameters from Roboteq board', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'load_roboteq', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 290, 'description': 'Restore to the original configuration', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'restore_defaults', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

RoboteqParameter_Clockwise = -1
RoboteqParameter_Counterclockwise = 1
RoboteqParameter_Disabled = 0
RoboteqParameter_250ms_at_10percent = 1
RoboteqParameter_500ms_at_25percent = 2
RoboteqParameter_1000ms_at_50percent = 3
