# SSH Key Uploader

Uploads a public key to server/s

## Getting Started

```
git clone https://github.com/kiminzajnr/Python_Projects.git
```

```
cd learner-pub-key-uploader
python3 -m venv .venv
. .venv/bin/activate
pip install Flask
```

```
python3 app.py
```
```
touch ~/.ssh/priv.key # add your private key here
chmod 400 ~/.ssh/priv.key
```


### Prerequisites

Refer to `Getting Started`


## Deployment

On your server:

```
touch ~/.ssh/priv.key # add your private key here
chmod 400 ~/.ssh/priv.key
```
```
git clone https://github.com/kiminzajnr/Python_Projects.git
```
```
cd learner-pub-key-uploader
python3 -m venv .venv
. .venv/bin/activate
pip install Flask
pip install gunicorn
```
```
touch wsgi.py
```
```
vi wsgi.py
```
and add:
```
from app import app


if __name__ == "__main__":
    app.run()

```
```
gunicorn --bind 0.0.0.0:5000 wsgi:app
```
```
deactivate
```
```
sudo vi /etc/systemd/system/app.service
```
and add
```
[Unit]
Description=Gunicorn instance to server app Flask app
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/My_App/learner-pub-key-uploader
Environment="Path=/home/ubuntu/My_App/learner-pub-key-uploader/.venv/bin"
ExecStart=/home/ubuntu/My_App/learner-pub-key-uploader/.venv/bin/gunicorn --workers 3 --bind unix:app.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```
```
sudo systemctl start app
```
```
sudo systemctl enable app # You might have to run sudo systemctl daemon-reload first
```
```
sudo systemctl status app # Should be active and running
```
```
sudo apt install nginx
```
```
sudo vi /etc/nginx/site-available/app.conf
```
and add:
```
server {
        listen 80;
        server_name alx1.parallel-cumpus.tech;

        location / {
                include proxy_params;
                proxy_pass http://unix:/home/ubuntu/learner-pub-key-uploader/app.sock;
        }
}

```
```
sudo ln -s /etc/nginx/site-available/app.conf /etc/nginx/site-enabled/
```
```
sudo nginx -t # test should be successful and syntax ok
```
```
sudo systemctl restart nginx
```
```
sudo ufw enable
sudo ufw allow ssh
sudo ufw allow "Nginx Full"
```
Test your app. If you get `502 Bad Gateway`, run:
```
sudo chmod 775 /home/user
```

> setting up https with let's encrypt
```
sud apt update; sudo snap install core; snap refresh core
```
```
sudo snap install --classic certbot
```
```
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```
```
sudo certbot --nginx
```

## Built with

- <img src="https://img.icons8.com/ios/452/flask.png" alt="Flask" width="20" height="20" style="filter: invert(45%) sepia(100%) saturate(2525%) hue-rotate(88deg) brightness(94%) contrast(91%);"/> [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- <img src="https://img.icons8.com/ios/452/console.png" alt="Bash" width="20" height="20" style="filter: invert(45%) sepia(100%) saturate(2525%) hue-rotate(88deg) brightness(94%) contrast(91%);"/> [Bash](https://www.gnu.org/software/bash/)
- <img src="https://www.w3.org/html/logo/downloads/HTML5_Logo_512.png" alt="HTML" width="20" height="20"/> [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- <img src="https://cdn.iconscout.com/icon/free/png-512/css3-9-1175237.png" alt="CSS" width="20" height="20"/> [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
