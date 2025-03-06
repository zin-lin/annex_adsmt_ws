# Feb Third+Fourth Week Slides

- ref
  - `NXDD` - highest next day delivery `priority`  
  - `P0` - highest `priority`
  - `P1` - high `priority`
  - `P2` - low `priority`
  - `O1` - optional `priority`
---

![Image](../showcase/adsmt.png)

---

# Recent Advancement Summary
- added equations for `kinematic` models
- finished the methodology 
- starting to focus on the test `results`

---


## URDF, RViz and Gazebo, Simulation Tests
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/gazebo/gazebo-original.svg" alt="Sample" width="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytorch/pytorch-original.svg" alt="Sample" width="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/ros/ros-original.svg" alt="Sample" width="50">

- refactoring has been done
- ai_simulation_package has been initialised
  - This will be using the `stable-baseline3` to train the robot
- test `drivers` are added in the `test_driver_package` taking the `bottom-up` testing approach.
  - `ai2vcu.launch.py` or path_planning to vehicle control
  - `gui_con2vcu.launch.py` or ui control to vehicle control
  - `sim2vcu.launch.py` or simulation nodes to vehicle control
  - `ter_con2vcu.launch.py` or terminal control to vehicle control

![Demo](../../docs/showcase/drive-demo.png) 

---

## Current System Stats
| Indicators             | Passed | Not Yet Capable | Will Not be Done |
|------------------------|--------|-----------------|------------------|
| Builds                 | ✅      | -               | -                |
| Autonomous             | ✅      | -               | -                |
| Simulation             | ✅      | -               | -                |
| Training               | -      | ✅               | -                |
| Walk                   | ✅      | -               | -                |
| Sim-Walk               | ✅      | -               | -                |
| Drive-Turn             | ✅      | -               | -                |
| perception             | ✅      | -               | -                |
| path_planning          | ✅      | -               | -                |
| gazebo-build           | ✅      | -               | -                |
| software-documentation | ✅      | -               | -                |
___
## Meeting minutes
- from now on, meeting minutes will be recorded as per `project-management`
- will use `markdown` - `.md` format as per `project-management`
- current system stats table is the `brain-child` of the minimisation fix of the `IPO`
  - will be updated weekly.
---

## Dissertation - Methodology and Results and Discussion Progress
- The methodology is done
  - is awaiting `review`
- results and discussions are awaiting on test data analysis which will be done by Sunday.


---

## Going Forward
- get `results and discussion` done - `P1`
- get results analyse - `P0`
- start working on tested data - `P1`
- start working on physical data - `P1`
- start training for future purposes if time allows - `P2`
---
## Any Questions?

---

