#!/bin/bash



source activate talaikis && /usr/local/anaconda/envs/talaikis/bin/uwsgi --ini /home/talaikis/emperor.ini

source deactivate
