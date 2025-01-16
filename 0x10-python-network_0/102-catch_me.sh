#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me to receive "You got me!"
curl -sL -X GET 0.0.0.0:5000/catch_me --data "user_id=98" -H "Origin: HolbertonSchool"
