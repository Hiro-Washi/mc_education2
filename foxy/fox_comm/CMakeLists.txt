cmake_minimum_required(VERSION 3.5)
project(fox_comm)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# ���C�u�����ˑ��֌W�̐ݒ�
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(fox_test_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# �ʐM���b�Z�[�W�̐ݒ�
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/RpsDo.srv"
)
ament_export_dependencies(rosidl_default_runtime)

# ���s�\�ɂ���C++�m�[�h��C�ӂ̕ϐ��icpp_exec�j�Ɋi�[���A�ǉ�
add_executable(cpp_exec
  src/ros2_comm_tmp.cpp
  src/rps_learn.cpp
  src/rps_hand_generator.cpp
)
# ��̊eC++�m�[�h�Ŏg��ROS2���C�u�����̈ˑ��֌W��ݒ�
ament_target_dependencies(cpp_exec
  rclcpp
  std_msgs
)
# 
install(TARGETS cpp_exec
  DESTINATION lib/${PROJECT_NAME}
)

# Python�ݒ�
ament_python_install_packages(${PROJECT_NAME})
# ���s����python�m�[�h�̃��C�u�����ˑ��֌W��ݒ�
install(PROGRAMS
  scripts/fox_comm_tmp.py
  DESTINATION lib/${PROJECT_NAME}
)

# �g���f�B���N�g����ݒ�
install(DIRECTORY
  src include scripts launch
  DESTINATION share/${PROJECT_NAME}
)
# �C���N���[�h�f�B���N�g����ݒ�
include_derectories(include)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()