# set base image (host OS)
FROM python:3.6

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY app/ .

# command to run on container start
RUN pip3 install submit50
RUN pip3 install --upgrade submit50
CMD ["python3"]
CMD tail -f /dev/null
