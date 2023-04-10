#!/bin/bash

HOME_DIR=/home/vagrant

sudo apt update
sudo apt install -y \
    curl nginx supervisor python3 python3-pip redis-server
# curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash

sudo cp -r $HOME_DIR/todo_infra/conf.d/sites-available/ /etc/nginx/
sudo cp $HOME_DIR/todo_infra/conf.d/supervisord.conf /etc/supervisor/
sudo cp $HOME_DIR/todo_infra/conf.d/gunicorn.conf /etc/supervisor/conf.d/
sudo cp $HOME_DIR/todo_infra/conf.d/nginx.conf /etc/nginx/

redis-server --daemonize yes --port 7777
sudo service supervisor restart

if [ ! -f /etc/nginx/sites-enabled/todo.local.conf ]; then
    sudo ln -s /etc/nginx/sites-available/todo.local.conf /etc/nginx/sites-enabled/todo.local.conf
fi

if [ ! -f /etc/nginx/sites-enabled/api.todo.local.conf ]; then
    sudo ln -s /etc/nginx/sites-available/api.todo.local.conf /etc/nginx/sites-enabled/api.todo.local.conf
fi

sudo systemctl restart nginx
