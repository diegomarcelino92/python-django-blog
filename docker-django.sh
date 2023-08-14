#!/bin/sh

alias docker="colima nerdctl --"
alias docker-compose="colima nerdctl -- compose"
docker exec django-blog python manage.py $1
