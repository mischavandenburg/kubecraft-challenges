# The Challenge: "Who Can Make This Docker Image the Smallest?"

## Your Mission

Your mission is to optimize the provided Dockerfile to create the smallest possible image while ensuring the application still runs correctly.

### Requirements

1. The image must run the Python application in `main.py` successfully
2. The Flask application must be accessible on port 8000
3. The application must use the dependencies specified in the pyproject.toml
4. You must use `uv` to manage the Python dependencies

### What's Provided

This repository contains:

- A bloated Dockerfile (approximately 1GB+ when built!)
- A simple Flask application in `main.py`
- A `pyproject.toml` with the necessary dependencies

## Hints

- Check out the documentation for [uv in Docker](https://astral.sh/uv/docs/integrations/docker)
- Consider what base image is truly necessary
- Think about which dependencies are actually needed at runtime vs. build time
- Remember that uv has special features for Docker optimization
- Remove anything from the Dockerfile that's not needed. This includes environment variables that are not needed for our program!

Good luck! Let's see who can create the most efficient container!

~ Mischa
