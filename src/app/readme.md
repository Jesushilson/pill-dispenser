
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz
tar -xvzf ngrok-v3-stable-linux-*.tgz
sudo mv ngrok /usr/local/bin
ngrok version

ngrok config add-authtoken 3A1eIOg3ixlbNE2Ghc3luxoYoBu_7BjMYgftYLjqye4v8drw8

ngrok http 5000

