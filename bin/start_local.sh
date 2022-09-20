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

echo "starting app for local dev"
TARGET_DIR="$1" uvicorn app.main:app --host 0.0.0.0 --port 80 --reload
