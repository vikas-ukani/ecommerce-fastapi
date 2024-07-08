FROM python:3.10
RUN pip install --upgrade pip
WORKDIR /
COPY ./main.py /main.py
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt
COPY ./app /app

CMD ["fastapi", "run", "app/main.py", "--port", "8001"]
EXPOSE 8001
