from fabric import Connection

with Connection(host='18.207.142.83',
                user='ubuntu',
                connect_kwargs={
                   'key_filename':'/home/erick/.ssh/priv.key',
                },
                ) as c:
                    c.local('mkdir -p versions')
                    c.local('touch versions/simple_file')
                    c.local('echo File to upload > versions/simple_file')
                    c.put('versions/simple_file', remote='/tmp')
                    c.run('sudo mkdir -p /data/web_static/releases/test/')
                    c.run('sudo touch /data/web_static/releases/test/index.html')
                    c.run('sudo ln -sf /data/web_static/releases/test/ /data/web_static/current')
                    c.run('sudo chown -R ubuntu:ubuntu /data/')
                    c.run('sudo apt update -y && sudo apt install nginx -y')
                    c.local('tar cvf versions/static_archive.tar web_static')
                    c.put('versions/static_archive.tar', remote='/data/web_static/current')
                    c.run('tar xf /data/web_static/current/static_archive.tar --directory=/data/web_static/current/')
                    c.run('rm /data/web_static/current/static_archive.tar')