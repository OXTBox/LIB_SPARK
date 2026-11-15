# Slide Ice Cave
PITCH: Players slide across an icy cave floor with arrow keys until a wall or rock stops them, collecting crystals for bonus points while reaching the exit hole. It is fun because the smooth sliding motion creates fast, predictable arcade movement with clear scoring goals.
CONTROLS: Use the arrow keys to move and Space to activate the exit.
OBJECTS:
- Ice floor | box 900,600 | cyan | provides smooth sliding movement when moved
- Wall | box 120,120 | blue | stops the player from sliding further
- Rock | box 80,80 | green | stops the player from sliding further
- Rough patch | box 60,60 | orange | stops the player early during sliding
- Crystal | box 30,30 | white | adds bonus score when collected
- Exit hole | box 40,40 | yellow | completes the level for a win
RULES:
- The player slides continuously in the direction of the arrow key until a wall, rock, or rough patch stops movement.
- Collecting a crystal grants 100 bonus points toward the final score.
- Each life allows three successful level completions before the game ends.
- Moving into a wall, rock, or rough patch costs one life if the player is not stopped by the patch.
- Reaching the exit hole clears the current level and starts the next one.
WIN: The player collects all crystals and reaches the exit hole to complete the final level.
LOSE: The player runs out of lives before completing all levels.
NUMBERS: player_speed=120, wall_count=3, rock_count=4, crystal_count=2, life_start=3, level_count=5
RISK: Programming the precise collision detection for ice sliding that stops only at specific obstacle shapes while handling rough patches that interrupt the slide without breaking the continuous movement.
