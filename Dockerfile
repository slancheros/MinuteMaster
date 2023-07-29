FROM python:3.10-slim

WORKDIR /meeting_ai

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install git -y
RUN pip3 install -r requirements.txt
RUN apt-get install -y ffmpeg

COPY . .

EXPOSE 7860

ENTRYPOINT [ "python3", "ui.py"]
##CMD [ "python3", "ui.py"]