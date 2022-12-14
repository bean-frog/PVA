if ! [ -x "$(command -v pip)" ]; then
  echo "Your don't have pip installed, installing it for you..."
  sudo apt-get install python-pip
fi
echo "Installing required module: playsound"
pip install playsound
read -p "Run PVA now? [type yes/no] " response

if [ "$response" == "yes" ]; then
  python PVA-Linux.py
fi
