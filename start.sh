#!/bin/bash

# Start Dagit in the background
dagit -h 0.0.0.0 -p 3000 -w workspace.yaml &
# Start Jupyter Notebook
exec jupyter notebook --ip='*' --port=8888 --no-browser --allow-root
