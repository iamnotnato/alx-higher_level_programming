#!/bin/bash
# Script that makes a request to causes an specific response
#curl -XPUT -d 'You got me!' -sL 0.0.0.0:5000/catch_me
curl -sL 0.0.0.0:5000/catch_me_2 -X PUT -d "user_id=98" -H "Origin: School"
