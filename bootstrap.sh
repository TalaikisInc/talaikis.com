#!/usr/bin/env bash

mkdir /home/talaikis
mkdir /home/talaikis/logs
mkdir /etc/uwsgi3
mkdir /etc/uwsgi3/vassals
ln /home/talaikis/uwsgi.ini /etc/uwsgi3/vassals/talaikis.ini
ln /home/talaikis/nginx_ssl.conf /etc/nginx/sites-enabled/talaikis.conf

source activate talaikis
cd /home/talaikis
pip install -r requirements.txt
source deactivate
chmod +x uwsgi.sh

sudo chown -R www-data:www-data /etc/uwsgi3
sudo chown -R www-data:www-data /home/talaikis

sudo cat << 'EOF' >> /etc/systemd/system/uwsgi3.service
[Unit]
Description=uwSGI

[Service]
WorkingDirectory=/home/talaikis
User=root
Group=root
Type=forking
ExecStart=/bin/bash /home/talaikis/uwsgi.sh

[Install]
WantedBy=multi-user.target
EOF

service uwsgi3 start
