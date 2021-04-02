#!/bin/bash

chown -R template:template /data/nr
chown -R template:template /root
uwsgi --ini uwsgi.ini
