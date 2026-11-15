# Counterweight Room
PITCH: Walk through the room using pulleys and crates to lift yourself toward the exit, solving the room's counterweight puzzle for a satisfying arcade challenge. It is fun because every move directly affects your path, creating a tight and rewarding puzzle experience.
CONTROLS: Arrow keys only. Walking into crates picks them up, pushes them, and presses switches.
OBJECTS:
- crate | box w=120 h=80 | wireframe grey | can be pushed by walking into it, acts as a counterweight on pulleys, and can be placed on platforms
- platform | box w=200 h=20 | wireframe brown | supports crates and provides a stable surface to lift yourself onto
- pulley | box w=40 h=60 | wireframe black | connects to crates to transfer weight, lifting platforms when the counterweight is heavier
- exit | box w=80 h=100 | wireframe green | the goal location, reached after lifting yourself onto a platform
RULES:
- Walking into a crate picks it up and you can push it in any direction with arrow keys.
- Crates push platforms upward when the opposite end of the pulley system is heavier.
- Push crates onto platforms to lift yourself to the exit.
- Score increases by 1 point for each crate successfully placed on a platform.
- Losing a life occurs when you fall off the room floor.
WIN: Reach the exit after lifting yourself onto a platform with all crates placed correctly.
LOSE: Falling off the room floor ends a try.
NUMBERS: crates=2, platforms=3, pulleys=2, exit=1, lives=3, score=0, speed=120
RISK: Programming the counterweight physics to accurately transfer weight between crates and platforms while keeping the wireframe rendering consistent with the 1983 arcade style.
