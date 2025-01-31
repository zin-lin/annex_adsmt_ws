cmake_minimum_required(VERSION 3.5)
project(adsmt_description)

# Find required packages
find_package(ament_cmake REQUIRED)

# Install the URDF and STL files
install(
  DIRECTORY simulation/
  DESTINATION share/${PROJECT_NAME}/simulation
)

install(
  DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

# Export package dependencies
ament_package()




