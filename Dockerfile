FROM python:3-alpine

ADD zombie_spawn.py /zombie_spawn.py

ENTRYPOINT ["python", "/zombie_spawn.py"]
