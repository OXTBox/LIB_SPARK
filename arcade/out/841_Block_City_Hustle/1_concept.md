# Block City Hustle
PITCH: Walk through a colorful top-down city, take cars, and complete ringing phone booth jobs to score points while keeping your heat meter low. It is fun because you can freely explore the streets, use cars to move fast, and manage your heat level to stay safe in the city.
CONTROLS: Use arrow keys to move, Space to take a car or start a job.
OBJECTS:
- car | box w=120 h=60 | colour=teal | lets you move faster through the city streets
- package | box w=40 h=40 | colour=orange | must be delivered to the phone booth to score points
- phone booth | box w=80 h=80 | colour=blue | rings to offer a job, such as delivering a package or chasing a target
- patrol car | box w=100 h=100 | colour=red | chases you when your heat meter is high, causing damage
- heat meter | box w=120 h=40 | colour=amber | tracks trouble caused by jobs, cleared by visiting a paint shop
RULES:
- Arrow keys move you through the city streets at normal speed.
- Taking a car increases your movement speed for a short time.
- Completing a phone booth job adds points to your score.
- Causing trouble raises the heat meter from 1 to 5 stars.
- Patrol cars chase you when the heat meter is high, costing lives.
- Visiting a paint shop clears the heat meter and stops the chase.
WIN: Complete all available phone booth jobs in the city to reach the target score.
LOSE: Lose all your lives when patrol cars catch you while the heat meter is high.
NUMBERS: speed=150, lives=3, score=0, heat=1, levels=3
RISK: Programming the dynamic patrol car chase and heat meter interactions that react to player actions in real time.
