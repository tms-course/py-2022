sudo apt update
sudo apt install -y \
    nginx supervisor python3 python3-pip

sudo cp -r /home/vagrant/todo_infra/conf.d/sites-available/ /etc/nginx/
sudo cp /home/vagrant/todo_infra/conf.d/supervisord.conf /etc/supervisor/
sudo cp /home/vagrant/todo_infra/conf.d/gunicorn.conf /etc/supervisor/conf.d/
sudo cp /home/vagrant/todo_infra/conf.d/nginx.conf /etc/nginx/

sudo service supervisor restart

if [ ! -f /etc/nginx/sites-enabled/todo.local.conf ]; then
    sudo ln -s /etc/nginx/sites-available/todo.local.conf /etc/nginx/sites-enabled/todo.local.conf
fi

if [ ! -f /etc/nginx/sites-enabled/api.todo.local.conf ]; then
    sudo ln -s /etc/nginx/sites-available/api.todo.local.conf /etc/nginx/sites-enabled/api.todo.local.conf
fi

sudo systemctl restart nginx
