
if ! [ -x "$(command -v pip)" ]; then
  echo "Installing pip..."
  sudo apt-get install python-pip
fi

echo "Installing required module: playsound"
pip install playsound
read -p "Launch PVA now? [type yes/no]" response

if [ "$response" == "yes" ]; then
  # Run the macos.py script if the response is yes
  python PVA-MacOS.py
fi






