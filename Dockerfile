FROM python:3

# We want proper container logging
ENV PYTHONUNBUFFERED 1

# Move requirements file into container
ADD requirements.txt /multiroom-chatbot/requirements.txt

# Set working directory to project
WORKDIR /multiroom-chatbot/

# Upgrade pip
RUN pip install --upgrade pip
# Install requirements
RUN pip install -r requirements.txt