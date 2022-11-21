FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
# install deps
RUN apt update && apt install -y python3 python3-pip build-essential tesseract-ocr libtesseract-dev ffmpeg libsm6 libxext6

RUN pip3 install Flask opencv-python Numpy==1.16 pytesseract pillow shapely

WORKDIR /app
# copy
COPY app.py /app/app.py
#COPY main.py .
COPY static /app/static
COPY templates/index.html /app/index.html
COPY templates/base.html /app/base.html
COPY tess_dict /app/tess_dict
COPY textdetect /app/textdetect

EXPOSE 5000

CMD [ "python3","app.py" ]