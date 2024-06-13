FROM python:3
WORKDIR /app
COPY . /app
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]