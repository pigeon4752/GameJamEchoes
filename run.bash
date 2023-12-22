#!/bin/bash
echo "Installing requirements..."
pip install -r requirements.txt
echo "Done."

echo "Starting the script"
python main.py