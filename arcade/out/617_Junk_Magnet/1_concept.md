# Junk Magnet
PITCH: You control a crane magnet that automatically collects metal under it, then drop it into the crusher to score points before the magnet overheats. It is fun because the simple arrow controls create a fast, satisfying loop of collecting and crushing metal.
CONTROLS: Use the arrow keys only. The left and right arrows move the crane horizontally, and the down arrow drops the magnet into the crusher.
OBJECTS:
- magnet | box w=40 h=20 | wireframe cyan | attracts and collects metal under it automatically
- crusher | box w=200 h=100 | wireframe orange | accepts dropped metal to score points
- metal | box w=30 h=30 | wireframe yellow | collectible scrap that the magnet picks up
RULES:
- The magnet moves with the crane and automatically collects metal that is directly under it.
- Dropping the magnet into the crusher scores one point per metal piece collected.
- The magnet overheats after 3 drops, ending the current try.
- The crane cannot move while the magnet is dropped into the crusher.
WIN: The player finishes the try with the magnet safely dropped into the crusher and the magnet cool.
LOSE: The magnet overheats after 3 drops, ending the current try.
NUMBERS: magnet_overheat_steps=90, crusher_score_per_drop=1, crane_speed=120, screen_width=900, screen_height=600
RISK: Automatically collecting metal under the magnet while keeping the magnet within safe drop boundaries without overheating during the drop phase.
