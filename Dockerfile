# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.7

WORKDIR /code 

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt 

COPY ./app /code/app

ENV TARGET_DIR="/code/workdir"

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
