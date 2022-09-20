#! /bin/sh

#TODO: throw error if missing the value
export TARGET_DIR="$1"

# probably want to make this compose up / compose down
docker build -t app_image .
docker run -d --rm -v $TARGET_DIR:/code/workdir --name app_container -p 80:80 app_image
