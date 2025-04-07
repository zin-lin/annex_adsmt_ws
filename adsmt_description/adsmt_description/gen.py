import math



def generate_straight():
    pass

apac = [
    (0.2, 3.4),
    (0.6, 3.7),
    (1.0, 3.8),
    (1.4, 3.8),
    (1.8, 4.1),
    (2.0, 4.5),
    (2.1, 5.0),
    (2.1, 5.3),
    (2.1, 5.8),
    (2.1, 6.1),
    (2.1, 6.4),
    (2.1, 6.7),
    (2.1, 7.0),
]

def generate_midpoints():
    points = [(0,0)]
    x = 0
    y = 0
    for i in range(10):
        x +=0.3
        point = (x, y)
        points.append(point)

    count = 0
    del_x = 0.3 * (math.sin(33))
    del_y = 0.3 * (math.cos(33))
    while  count < len(apac):
        points.append((apac[count][1], apac[count][0]))
        count += 1

    return points

def generate_pair(px):
    points = []
    count = 0
    for i in px:
        if count == 0:
            points.append((0.0, 0.5))
            count += 1
            continue
        prev = px[count-1]
        x1 = prev[0]
        y1 = prev[1]
        x2 = i[0]
        y2 = i[1]

        theta = 0.0
        try:
            theta = math.atan((y2 - y1)/ (x2 - x1))
        except ZeroDivisionError:
            theta = 0.0

        hypo = 0.5
        x_new = hypo * math.sin(theta)
        y_new = hypo * math.cos(theta)

        x_fin = x2 - x_new
        y_fin = y2 + y_new
        points.append((x_fin, y_fin))
        count += 1

    return points

# pop = generate_midpoints()
# print(pop)
# for xxd in pop:
#     print(f"({xxd[1]}, {xxd[0]})\n")
#
# print('xxx')
#
# pp = generate_pair(pop)
# print(pp)
# for xxd in pp:
#     print(f"({xxd[1]}, {xxd[0]})\n")
#


#
# def generate_sdf():
#     sdf_content = '''<?xml version="1.0"?>
# <sdf version="1.6">
#   <world name="default">
# '''
#
#     # Initial position and direction
#     x = 0.0
#     y = 0.0
#     orientation = 0.0  # Angle of the path in radians
#
#     # Function to create a pair of cones
#     def add_cone_pair(x, y, orientation, index):
#         # Adjust left and right cone placement for 60 cm track width (30 cm on each side)
#         left_x = x   # 60 cm apart, left
#         left_y = y + math.sin(orientation + math.pi / 2) * 0.3
#         right_x = x
#         right_y = y + math.sin(orientation - math.pi / 2) * 0.3
#
#         sdf_content = f'''
#         <model name="left_cone_{index}">
#           <link name="link">
#             <pose>{left_x} {left_y} 0.025 0 0 0</pose>
#             <collision name="collision">
#               <geometry>
#                 <cylinder>
#                   <radius>0.015</radius>
#                   <length>0.05</length>
#                 </cylinder>
#               </geometry>
#             </collision>
#             <visual name="visual">
#               <geometry>
#                 <cylinder>
#                   <radius>0.015</radius>
#                   <length>0.05</length>
#                 </cylinder>
#               </geometry>
#               <material>
#                 <ambient>1 0 0 1</ambient>
#                 <diffuse>1 0 0 1</diffuse>
#               </material>
#             </visual>
#           </link>
#         </model>
#
#         <model name="right_cone_{index}">
#           <link name="link">
#             <pose>{right_x} {right_y} 0.025 0 0 0</pose>
#             <collision name="collision">
#               <geometry>
#                 <cylinder>
#                   <radius>0.015</radius>
#                   <length>0.05</length>
#                 </cylinder>
#               </geometry>
#             </collision>
#             <visual name="visual">
#               <geometry>
#                 <cylinder>
#                   <radius>0.015</radius>
#                   <length>0.05</length>
#                 </cylinder>
#               </geometry>
#               <material>
#                 <ambient>0 0 1 1</ambient>
#                 <diffuse>0 0 1 1</diffuse>
#               </material>
#             </visual>
#           </link>
#         </model>
#     '''
#         return sdf_content, left_x, left_y, right_x, right_y
#
#     # Function to create a pair of cones
#     def add_cone_pair_curve(x, y, orientation, index):
#         # Adjust left and right cone placement for 60 cm track width (30 cm on each side)
#         left_x = x + math.cos(orientation + math.pi/2) * 0.3  # 60 cm apart, left
#         left_y = y + math.sin(orientation + math.pi/2) * 0.3
#         right_x = x + math.cos(orientation - math.pi/2) * 0.3  # 60 cm apart, right
#         right_y = y + math.sin(orientation - math.pi/2) * 0.3
#
#         sdf_content = f'''
#     <model name="left_cone_{index}">
#       <link name="link">
#         <pose>{left_x} {left_y} 0.025 0 0 0</pose>
#         <collision name="collision">
#           <geometry>
#             <cylinder>
#               <radius>0.015</radius>
#               <length>0.05</length>
#             </cylinder>
#           </geometry>
#         </collision>
#         <visual name="visual">
#           <geometry>
#             <cylinder>
#               <radius>0.015</radius>
#               <length>0.05</length>
#             </cylinder>
#           </geometry>
#           <material>
#             <ambient>1 0 0 1</ambient>
#             <diffuse>1 0 0 1</diffuse>
#           </material>
#         </visual>
#       </link>
#     </model>
#
#     <model name="right_cone_{index}">
#       <link name="link">
#         <pose>{right_x} {right_y} 0.025 0 0 0</pose>
#         <collision name="collision">
#           <geometry>
#             <cylinder>
#               <radius>0.015</radius>
#               <length>0.05</length>
#             </cylinder>
#           </geometry>
#         </collision>
#         <visual name="visual">
#           <geometry>
#             <cylinder>
#               <radius>0.015</radius>
#               <length>0.05</length>
#             </cylinder>
#           </geometry>
#           <material>
#             <ambient>0 0 1 1</ambient>
#             <diffuse>0 0 1 1</diffuse>
#           </material>
#         </visual>
#       </link>
#     </model>
# '''
#         return sdf_content, left_x, left_y, right_x, right_y
#
#     # First 10 pairs of cones in a straight line
#     for i in range(10):
#         sdf, x, y, _, _ = add_cone_pair(x, y, orientation, i)
#         sdf_content += sdf
#         x +=  0.2  # Move 20 cm straight along the x-axis
#
#
#     # Gradual 90-degree right turn over 4 pairs
#     for i in range(10, 14):
#         sdf, x, y, _, _ = add_cone_pair_curve(x, y, orientation, i)
#         sdf_content += sdf
#         x += math.cos(orientation) * 0.2
#         y += math.sin(orientation) * 0.2
#         orientation += math.radians(20)  # Increase orientation by 20 degrees per pair
#
#     # Add 4 pairs after the turn
#     for i in range(14, 18):
#         sdf, x, y, _, _ = add_cone_pair(x, y, orientation, i)
#         sdf_content += sdf
#         x += math.cos(orientation) * 0.2
#
#
#     # Gradual 90-degree left turn over 4 pairs
#     for i in range(18, 22):
#         sdf, x, y, _, _ = add_cone_pair_curve(x, y, orientation, i)
#         sdf_content += sdf
#         x += math.cos(orientation) * 0.2
#         y += math.sin(orientation) * 0.2
#         orientation -= math.radians(20)  # Decrease orientation by 20 degrees per pair
#
#     # Add another straight line with 10 pairs of cones
#     for i in range(22, 32):
#         sdf, x, y, _, _ = add_cone_pair(x, y, orientation, i)
#         sdf_content += sdf
#         x += 0.2
#
#     # Closing tags
#     sdf_content += '''
#   </world>
# </sdf>
# '''
#
#     # Write the generated SDF to a file
#     with open("generated_world.sdf", "w") as f:
#         f.write(sdf_content)
#
#     print("SDF file generated successfully: generated_world.sdf")
#
# # Call the function to generate the SDF
# generate_sdf()


right = [(0.0, 0.5), (0.3, 0.5), (0.6, 0.5), (0.8999999999999999, 0.5), (1.2, 0.5), (1.5, 0.5), (1.8, 0.5), (2.1, 0.5), (2.4, 0.5), (2.6999999999999997, 0.5), (2.9999999999999996, 0.5), (3.176393202250021, 0.647213595499958), (3.3000000000000003, 0.9000000000000001), (3.3149287499273337, 1.121267812518166), (3.4, 1.6), (3.6999999999999993, 2.0999999999999996), (4.276393202250021, 2.447213595499958), (4.9019419324309075, 2.59029033784546), (5.3, 2.6), (5.8, 2.6), (6.1, 2.6), (6.4, 2.6), (6.7, 2.6), (7.0, 2.6)]
left_cones = [(0, 0), (0.3, 0), (0.6, 0), (0.8999999999999999, 0), (1.2, 0), (1.5, 0), (1.8, 0), (2.1, 0), (2.4, 0), (2.6999999999999997, 0), (2.9999999999999996, 0), (3.4, 0.2), (3.7, 0.6), (3.8, 1.0), (3.8, 1.4), (4.1, 1.8), (4.5, 2.0), (5.0, 2.1), (5.3, 2.1), (5.8, 2.1), (6.1, 2.1), (6.4, 2.1), (6.7, 2.1), (7.0, 2.1)]
right_cones = []
for r in right:
    new_r = (r[0], r[1]*1)
    right_cones.append(new_r)

def generate_right_cones():
    sdf = ""
    index = 0
    for rr in right_cones:
        sdf += f'''
        <model name="right_cone_{index}">
          <link name="link">
            <pose>{rr[0]} {rr[1]} 0.025 0 0 0</pose>
            <collision name="collision">
              <geometry>
                <cylinder>
                  <radius>0.015</radius>
                  <length>0.05</length>
                </cylinder>
              </geometry>
            </collision>
            <visual name="visual">
              <geometry>
                <cylinder>
                  <radius>0.015</radius>
                  <length>0.05</length>
                </cylinder>
              </geometry>
              <material>
                <ambient>0 0 1 1</ambient>
                <diffuse>0 0 1 1</diffuse>
              </material>
            </visual>
          </link>
        </model>
        
        '''
        index += 1

    return sdf


def generate_left_cones():
    sdf = ""
    index = 0
    for ll in left_cones:
        sdf += f'''
        <model name="left_cone_{index}">
          <link name="link">
            <pose>{ll[0]} {ll[1]} 0.025 0 0 0</pose>
            <collision name="collision">
              <geometry>
                <cylinder>
                  <radius>0.015</radius>
                  <length>0.05</length>
                </cylinder>
              </geometry>
            </collision>
            <visual name="visual">
              <geometry>
                <cylinder>
                  <radius>0.015</radius>
                  <length>0.05</length>
                </cylinder>
              </geometry>
              <material>
                <ambient>0 0 1 1</ambient>
                <diffuse>0 0 1 1</diffuse>
              </material>
            </visual>
          </link>
        </model>

        '''
        index += 1
    return sdf

sdf = ""
sdf += generate_right_cones()
sdf += generate_left_cones()

print (sdf)