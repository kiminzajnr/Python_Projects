# use the python:3.0 image as base
FROM python:3.10

# a documentation specifying port 5000 is something the container will use
EXPOSE 5000

# everything we do in docker image will happen in the images /app directory
WORKDIR /app

COPY requirements.txt .

# run command in image
RUN pip install flask

# coopies everything in the current folder into the images current folder
COPY . .

# tell the image what command to run when you start a containter flask run --host=0.0.0.0
CMD ["flask", "run", "--host", "0.0.0.0"]