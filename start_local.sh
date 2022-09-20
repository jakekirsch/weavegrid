#! /bin/sh
TARGET_DIR="$1" uvicorn app.main:app --host 0.0.0.0 --port 80 --reload
