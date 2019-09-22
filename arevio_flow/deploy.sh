#!/bin/sh

location="$HOME/arevio-flow/arevio_flow"

cd "$location" || { echo "Fail"; exit 1; }
rm -rf frontend/dist/
tar -xvf "$HOME/dist.tgz"

# Browser cache busting
epoch=$(date +%s)
file='./frontend/dist/bundle'
mv $file.js $file."$epoch".js
mv $file.css $file."$epoch".css

# Update index.html to reference those files
file='./templates/index.html'
cp --no-clobber $file $file.bak
script1="s/{% static 'bundle\.js' %}/\/static\/bundle.$epoch.js/"
script2="s/{% static 'bundle\.css' %}/\/static\/bundle.$epoch.css/"
sed -e "$script1; $script2" < $file.bak > $file

. "../venv/bin/activate"
python3 manage.py collectstatic --no-input
