import subprocess
from multiprocessing import Process
from time import sleep

if __name__ == '__main__':
    while True:
        print("spawning")
        for n in range(500):
            subprocess.Popen(["sleep", "1"])
            # Process(target=sleep, args=(1, ), daemon=True).start()

        sleep(4)

