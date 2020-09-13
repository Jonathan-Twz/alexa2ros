#!/bin/bash
#
# Loop through all the packages in ROS_PACKAGE_PATH 
# If we find our package and the amazon directory,
# run the ngrok program inside there.

IFS=":" 
path_found=false

for path in $ROS_PACKAGE_PATH
do
    ngrok_path="${path}/alexa2ros/src"
    #printf "\n$ngrok_path\n" 
    if [ -d "${ngrok_path}" ]; then
        path_found=true
        $ngrok_path/ngrok http --subdomain=hrlab-mini-cheetah --authtoken=5daaRdfBrYFFntbHe8XC_6VM5LLJcxiNAtD2yTqQZp 5000 
    fi
done


if [ ! $path_found ] ; then
    echo "Path to ngrok not found. Set your package path or add the alexa2ros repo to your workspace"
fi
