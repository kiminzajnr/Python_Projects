# Project Title

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

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds