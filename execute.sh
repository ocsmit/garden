#!/bin/sh

echo "Initializing garden"

python3.7 /home/pi/garden/garden.py

echo "Pictures saved"

git add -A
git commit -m "Update data"
git push 

echo "Images uploaded"

