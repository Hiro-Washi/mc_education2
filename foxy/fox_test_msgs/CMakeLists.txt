cmake_minimum_required(VERSION 3.5)
project(fox_test_msgs)

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
# 独自のメッセージを生成するのに使う。メッセージデータ構造の構築が可能
find_package(rosidl_default_generators REQUIRED)
#find_package(builtin_interfaces REQUIRED)


# 通信メッセージの設定
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/MyMessage.msg"
  "srv/ServiceTest.srv"
  # コンパイル後→ service_test.hpp
  "action/ActionTest.action"
)
ament_export_dependencies(rosidl_default_runtime)

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
