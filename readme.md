# Pid 1 Zombie problem

Ostensibly, there is a problem in Docker when PID 1 doesn't reap zombies, they 
can accumlate. This repo is trying to reproduce that issue to demonstrate that 
it needs to be resolved and provide a testbed for their resoltuion.

At the moment, the python zombie spawner does **not** work right and **doesn't** spawn
zombies.

