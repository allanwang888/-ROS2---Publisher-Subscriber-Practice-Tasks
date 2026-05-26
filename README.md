# ROS2 Publisher & Subscriber Hands-On Assignment

Hi there, below are two tasks designed to test your understanding of nodes, timers, topics, and workspaces. 

---

## Task 1: Modify the Publisher

Your first task is to modify the existing `simple_publisher.py` script to change its output data and frequency (NOTE: THE ONE THAT WE DID IN THE VIDEO - YOU HAVE TO MODIFY IT).

### ( Instructions ):
1. Open your `simple_publisher.py` file in your code editor.
2. **Change the message string** so that it publishes your own name.
3. **Modify the timer frequency** so that it publishes a message every **0.5 seconds** instead of the original 1.0 second.
4. Save your file.

### ( Crucial Step: Rebuild Your Workspace ):
Because you modified the source code, ROS2 will not see your changes until you rebuild. Run the following commands in your workspace root terminal:

# How to run your code after you have finished coding?
```bash
# 1. Build the workspace to register changes
colcon build

# 2. Refresh your terminal environment
source install/setup.bash

# 3. Run your updated node
ros2 run {your_package_name} {your_executable_name}
```

---

## Task 2: Create a Custom Theme Rewrite

Your second task is to rewrite both the publisher and subscriber nodes from scratch using a completely different theme of your choice.

Instead of generic text and a `'robot_news'` topic, choose a theme that interests you.

### ( Choose ONE below and start coding ):
* **(Space Mission)**: A satellite node publishing telemetry data (e.g., speed, altitude) to a ground control subscriber node on a `'satellite_data'` topic.
* **(Smart Home)**: A temperature sensor node publishing room readings to a central smart thermostat subscriber node on a `'home_temp'` topic.
* **(Gaming)**: A player node publishing live health points or high scores to a scoreboard subscriber node on a `'game_scores'` topic.

### ( Requirements ):
* Create a **brand-new package** or add new files to your existing package (the folder that has '__init__.py').
* Update your `setup.py` file with unique executable names for your new theme.
* Ensure your custom publisher and custom subscriber target the exact same topic name.
* Run `colcon build` and `source` your workspace to verify that your themed nodes communicate successfully in the terminal.


# ( If you are stuck, please look at the answer!)
