FROM python:3.7-slim as builder


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#creating a working directory
RUN mkdir /apps

# changing the default working of the container
WORKDIR /apps

ENV FLASK_RUN_HOST=0.0.0.0  

# copy the requirements file to the working directory
# working directory of your machine to working directory of Docker
COPY ./requirements.txt ./ 

# Install some depenendencies
RUN pip install -r requirements.txt

# copy the dependencies file to the working directory
COPY ./ ./ 


#nginx
FROM nginx
COPY --from=builder apps/ usr/share/nginx/html
