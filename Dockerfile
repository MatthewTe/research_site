#########################################################
# The Dockerfile for building and initalizing the Research
# Django Site
#########################################################
FROM python:3.8

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Copying the django site files into the container: 
COPY research_site /research_site
WORKDIR /research_site

# Installing python packages:
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Configuring and starting the Django Project via a bash script: 
ENTRYPOINT ["sh", "start_server.sh"]