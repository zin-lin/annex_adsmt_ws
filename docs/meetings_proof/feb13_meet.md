# Feb Second Week Slides

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
- added successful `amble-gait`
  - one-sided forward approach
- added successful `turn` walk 
- added successful `forward` jump 
  - all tested with `gazebo`
- added `adsmt-wheeled.xacro`
  - This adds modelled wheels
- added successful `drive-forward` mode
- added imbalance thrust turning during `drive` mode
- determined what data will be collected and analyse for the `empirical` research approach.
- determined the structure of the methodology - awaiting approval. 

---


## URDF, RViz and Gazebo, Simulation Tests
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/gazebo/gazebo-original.svg" alt="Sample" width="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytorch/pytorch-original.svg" alt="Sample" width="50">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/ros/ros-original.svg" alt="Sample" width="50">

- added wheels on the model of the `ads-mt`
- added `JointController` plugin under wheels to allow velocity commands
  - Tuning must be done with the actual robot to reflect similar velocity. 
  - `Drive` mode is working 
- The neural network theory is scrapped and to be implemented only if time allows for sake of narrowing the scope.
  - new priority `O1`
- Forward drive is achieved by allowing four wheels spin
- While walking one must lock `torque` on wheels to make forward movements
- `imbalance-velocity` is used for turning 
![Demo](../../docs/showcase/drive-demo.png) 
---

## Current System Stats
| Indicators    | Passed              | Not Yet Capable |
|---------------|---------------------|-----------------|
| Builds        | ✅                   | -               |
| Autonomous    | -                   | ✅               |
| Simulation    | ✅                   | -               |
| Training      | -                   | ✅               |
| Walk          | ✅ semi-functional   | -               |
| Sim-Walk      | ✅ functional-manual | -               |
| Drive         | ✅ functional-manual | -               |
| Drive-Turn    | ✅ functional-manual | -               |
| perception    | ✅                   | -               |
| path_planning | -                   | ✅               |
| gazebo-build  | ✅                   | -               |
___
## Meeting minutes
- from now on, meeting minutes will be recorded as per `project-management`
- will use `markdown` - `.md` format as per `project-management`
- current system stats table is the `brain-child` of the minimisation fix of the `IPO`
  - will be updated weekly.
---

## Dissertation - Methodology Structure

### 3. Methodology
#### 3.1 Research Methodology (300-400 words)
#### 3.2 Prototype Design 
  - ##### 3.2.1 Hardware Design (500 words)
  - ##### 3.2.2 Software Architecture (700 words)
  - ##### 3.2.3 Simulation Architecture (500 words)
  - ##### 3.2.3 Networking Architecture (500 words)
  - ##### 3.2.4 Kinematics and Controls 
    - ##### 3.2.4.1 Car-like Control (300 words)
    - ##### 3.2.4.2 Quadruped Control (300 words)
    - ##### 3.2.4.3 Hybrid Control (200 words)
    - ##### 3.2.4.3 Autonomous design (500 words)

#### 3.3 Data/Result Gathering and Evaluation pattern
  - #### 3.3.1 Real-world Kinematics and Behavioural Testing (300 words)
    - Real-world `Amble Gait`
      - Real-world `Turn Gait`
      - Real-world `Jump Gait`
      - Real-world `Drive` 
      - Real-world `Pure-pursuit `
      - Real-world `Hybrid` transition

- #### 3.3.2 Simulation Kinematics and Behavioural Testing (300 words)
  - Simulation `Amble Gait`
  - Simulation `Turn Gait`
  - Simulation `Jump Gait`
  - Simulation `Drive `
  - Simulation `Pure-pursuit`
  - Simulation `Hybrid` transition

    - While others are behavioural and test against time
  This will test against each algorithms, imbalance thrust or skater theory
  Simulation Autonomous Design - self error test regression
  This will be to use the superior hybrid algorithms

- ##### 3.3.3 Bridging Between Simulation and Real-world (200 words)
  - While autonomous design is purely sim a real-life test will be carried out to see how far the errors goes on longer distances.
#### 3.4 Data/Result Interpretation and Analysis
- ##### 3.3.1 Introduction (50-100 words)
- ##### 3.3.2 Quantitative Data (100 words) (real-world in sim)
	- Match quantitative 6 topics and comparison 
- ##### 3.3.2 Qualitative Data (100 words) (simulation only)
	- Cluster to find interesting groups of data 
	- Cluster between autonomous design data and calculated design 

#### 3.5 Ethical Considerations (200 words)

---

## Going Forward
- get `autonomous design` to work - `P1`
- get `hybrid design` to work - `NXDD`
- get `sim-perception` data to look at - `P1`
- get `sim-IMU` data to look at - `P0` 
  - important for data collection
---
## Any Questions?

---

