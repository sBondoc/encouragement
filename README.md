# Encouragement
For when you need to add a little brightness to your day. 🌄

## About
This app displays on the console a random phrase from a newline-separated list of strings in a `.txt` file stored on Google Drive.

## Setup
Developed for installation and use on a Linux machine with a web browser.

### Prerequisites
GNU `make` is required to run the installation makefile and may be installed with `apt-get`:
```
sudo apt-get install make
```
The Google Drive API's [Python implementation](https://developers.google.com/drive/api/quickstart/python "Quickstart documentation.") is used to retrieve data from cloud storage.

Required Google Drive API libraries may be installed using `pip`:
```
pip install --upgrade google-api-python-client google-auth-httplib2
```

### Installation
Clone the repository from GitHub:
```
git clone https://github.com/sBondoc/encouragement.git
```
From the root project directory, use `make` to install the configuration file:
```
make install
```
The makefile copies the template configuration file `data/config.cfg` locally to `~/.encouragement/config.cfg`.

### Configuration
A Google Drive file ID must be set in `~/.encouragement/config.cfg`.

Sample config file:
```ini
[gdrive]
fileid = 1OGLtMQgQ3TP-hwhOUQy_Tc0lqQ2yKI9L
```
Access credentials need to be created for the app. Follow the [Google documentation](https://developers.google.com/workspace/guides/create-credentials#oauth-client-id "Credential documentation.") on credential setup to obtain OAuth client ID credentials.

The resultant `credentials.json` file should be downloaded and placed `~/.encouragement/`.

## Usage
Run `script/app.py` using Python from the project root directory:
```
python script/app.py
```

You will be prompted to sign in to Google Drive on first execution to generate an access token at `~/.encouragement/token.json`.
