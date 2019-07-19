import subprocess
from time import sleep

if __name__ == '__main__':
    while True:
        print("spawning")
        for n in range(500):
            subprocess.Popen(["sleep", "1"])
        sleep(20)

