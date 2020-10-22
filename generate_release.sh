#!/bin/bash

RELEASE_VERSION=$1
mkdir bin
cp -r imd_forecast bin/imd_forecast
cd bin
pipenv lock -r > requirements.txt 
pip install -r requirements.txt --target imd_forecast

python -m zipapp -p "interpreter" imd_forecast

# cleanup
mv imd_forecast.pyz ../
cd ..
rm -rf bin
