#!/bin/bash

name="textdetectapp"

docker build -t $name .

docker run --rm -it -p 5000:5000 --device /dev/video0 -v $(pwd)/app.py:/app/app.py -v $(pwd)/textdetect/textdetect.py:/app/textdetect/textdetect.py $name
