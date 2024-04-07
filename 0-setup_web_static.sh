#!/usr/bin/env bash
#script to deploy web static

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

#creating directories

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

#creating a html file
sudo echo "<html>
<head>
</head>
<body>
    Holberton School
<body>
</html>" | sudo tee /data/web_static/releases/test/index.html

#create or upadate the symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

#changing ownership of /data/
sudo chown -R ubuntu:ubuntu /data/

#upddate nginx configuration to serve content from /data/web_static/current file
if ! sudo grep -q "alias /data/web_static/current/;" /etc/nginx/sites-enabled/default; then
    sudo sed -i "\#server_name _;#a \\
        location /hbnb_static { \\
            alias /data/web_static/current/; \\
        } \\
        " /etc/nginx/sites-enabled/default
fi

# restart it
sudo nginx -t
sudo systemctl restart nginx
