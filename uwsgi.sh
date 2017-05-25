#!/bin/bash

export LD_LIBRARY_PATH=/usr/local/anaconda/lib:$LD_LIBRARY_PATH

source /usr/local/anaconda/bin/activate /usr/local/anaconda/envs/talaikis && /usr/local/anaconda/envs/talaikis/bin/uwsgi --ini /home/talaikis/emperor.ini

source /usr/local/anaconda/bin/deactivate
