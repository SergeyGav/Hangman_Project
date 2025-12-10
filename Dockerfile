FROM ubuntu:resolute-20251101

RUN apt-get update
RUN apt-get install -y python3

COPY main_game.py /app/python/.
COPY game_functions /app/python/game_functions/.


CMD ["python3", "/app/python/main_game.py"]