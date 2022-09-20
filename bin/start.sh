#! /bin/sh

if [ -z "$1" ]
  then "No argument for root_dir supplied, try passing a directory"
  exit 1
fi

export TARGET_DIR="$1"

if [[ "$TARGET_DIR" != /* ]]
  then "root_dir must be an absolute path"
  exit 1
fi

docker build -t app_image .
docker run -d --rm -v $TARGET_DIR:/code/workdir --name app_container -p 80:80 app_image
