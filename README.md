# Docker Wrapper for the Mocro-Model Simulation of SWA Project

Be aware that this image is part of a larger project (swa-meshup) to develop/test the full setup, please 
However, this is an independant local service, that can be used for development. In the case of local development, you might want to change the docker-compose.yml in order to mount a local directory with proper test data to /rea-data instead of using a docker volume.

## Installation and Deplyoment

### Build the image

Run this command to create the image:
''' docker build -t fnyffene/swa-macromodel . '''

### Development Setup

For local development, just run 
''' docker-compose up '''
The local py files of this project will be mounted to the docker image.
Flask allows you to change the code and restart on the fly.

### Deployment

All pushes to the master branch will be deployed to appui automatically.

## API

Test if alive ''' GET /test '''
Start simulation ''' GET /start '''
