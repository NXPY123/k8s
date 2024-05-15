
import os
import datetime

# Pathway to folder I want to look through.

rootdir = os.getcwd()


manifest_file_location = rootdir + "/yaml/testapp-rollout.yaml"



manifest_file = open(manifest_file_location, 'w')

# find the "image: nxpy/k8s-flask-app:[VERSION]" line in the yaml file and replace it with the sha256 of the latest git commit
# this will trigger a rollout in the k8s cluster

# get the latest git commit from ${{ github.sha }}

sha = os.getenv('GITHUB_SHA')


# find the line in the yaml file that contains "image: nxpy/k8s-flask-app:[VERSION]"
# replace [VERSION] with the sha256 of the latest git commit

for line in manifest_file:
    if "image: nxpy/k8s-flask-app:" in line:
        line = "image: nxpy/k8s-flask-app:" + sha
    manifest_file.write(line)

manifest_file.close()