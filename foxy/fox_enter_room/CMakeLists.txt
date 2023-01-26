cmake_minimum_required(VERSION 3.5)
project(fox_enter_room)

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

# ライブラリ依存関係の設定
find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(rclpy REQUIRED)
find_package(rclcpp REQUIRED)

# 通信メッセージの設定
rosidl_generate_interfaces(${PROJECT_NAME}
  srv/EnterRoom.srv # コンパイル後→enter_room.hpp
)
ament_export_dependencies(rosidl_default_runtime)

# 実行可能にするC++ノードを任意の変数（cpp_exec）に格納し、追加
add_executable(cpp_exec
  src/fox_enter_room.cpp
)
# 上に書いた各C++ノードで使うROS2ライブラリの依存関係を設定
ament_target_dependencies(cpp_exec
  rclcpp
  std_msgs
  geometry_msgs
  sensor_msgs
)
# 
install(TARGETS cpp_exec
  DESTINATION lib/${PROJECT_NAME}
)

# 実行するpythonノードの設定
ament_python_install_packages(${PROJECT_NAME})
# 実行するpythonノードのライブラリ依存関係を設定
install(PROGRAMS
  scripts/fox_enter_room.py
  #scripts/fox_enter_room2.py
  DESTINATION lib/${PROJECT_NAME}
)

# 使えるようにしたいディレクトリを設定
install(DIRECTORY
  src srv include scripts launch
  DESTINATION share/${PROJECT_NAME}
)
# インクルードディレクトリを設定
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
