# pepper_tweeting

## Environment

* python2.7 (system python)

## Install

### Get python SDK

you have to download pepper-python-sdk and set env variables.

download from here
https://community.aldebaran.com/ja/

set $PYTHONPATH and $DYLD_LIBRARY_PATH like below.

* if you unzip sdk to ~/naoqi/pynaoqi-python2.7-2.1.4.13-mac64

```
export PYTHONPATH=${PYTHONPATH}:~/naoqi/pynaoqi-python2.7-2.1.4.13-mac64
export DYLD_LIBRARY_PATH=${DYLD_LIBRARY_PATH}:~/naoqi/pynaoqi-python2.7-2.1.4.13-mac64
```

reference here (japanese) http://qiita.com/Atelier-Akihabara/items/3289e60985586b8da709

### Install pepper_tweeting

```bash
$ git clone https://github.com/shiraco/pepper_tweeting.git
$ cd pepper_tweeting
$ pip install -r requirements.txt
```

## Setting API KEY

Get Twitter API KEY

https://dev.twitter.com/

Set api keys to your application

```bash
$ cp .env.sample .env
$ vi .env  # update your api key
$ source .env  # apply api key as a environment variable
```

## Usage

```bash
% python pepper_tweeting.py "192.168.0.9" "#pepper_say"
```
