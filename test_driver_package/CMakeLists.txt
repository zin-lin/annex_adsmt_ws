cmake_minimum_required(VERSION 3.5)
project(test_driver_package)

# Find required packages
find_package(ament_cmake REQUIRED)

# Install Launch
install(
  DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

# Export package dependencies
ament_package()




