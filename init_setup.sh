#!/bin/bash

VERSION=3.8

echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python $VERSION"
conda create --prefix ./env python=$VERSION -y

echo [$(date)]: "Activating env"
source activate ./env || conda activate ./env

echo [$(date)]: "Installing dev requirements"
pip install -r requirements_dev.txt

echo [$(date)]: "END"
