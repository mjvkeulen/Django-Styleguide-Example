# This docker file is used for local development via docker-compose
# Creating image based on official python3 image
FROM python:3.12.4

# Fix python printing
ENV PYTHONUNBUFFERED 1

# Installing all python dependencies
ADD requirements/ requirements/
RUN pip install -r requirements/local.txt

# devcontainer dependencies and utils
RUN apt-get update && apt-get install --no-install-recommends -y \
    sudo git bash-completion nano ssh vim \
    # TODO STACK: Can be removed once we have devcontainer
    && apt-get install -y zsh \
    && wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true \
    && chsh -s $(which zsh)

# Get the django project into the docker container
RUN mkdir /app
WORKDIR /app
ADD ./ /app/
