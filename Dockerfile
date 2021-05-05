FROM python:3.7-slim
ADD ./backend/src /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py

