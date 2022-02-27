# Containerized_microservice_deploy_AWS
[![Python application test with Github Actions](https://github.com/kaifeng-yu16/Containerized_microservice_deploy_AWS/actions/workflows/main.yml/badge.svg)](https://github.com/kaifeng-yu16/Containerized_microservice_deploy_AWS/actions/workflows/main.yml)

This is duke ids 721 project2. This project builds a translation and text generation microservice using Flask. The microservice is containerized using docker and pushed to both AWS ECR and Dockerhub. It is finally deployed using AWS App Runner.

## How to use
To use this app, go to website https://3m6az7rvsu.us-east-1.awsapprunner.com/, choose "Translate" if you want to do translation tasks or choose "Tell a Story" if you wan to do text generation tasks.

![image](https://user-images.githubusercontent.com/90477174/155877608-e11cd9d8-3656-4ab3-8c20-062a46a67bc8.png)

![image](https://user-images.githubusercontent.com/90477174/155877624-07fa8a82-5442-476c-8d0c-6593793621aa.png)

![image](https://user-images.githubusercontent.com/90477174/155877649-97cd0346-a7b9-4cdc-bdc5-453b12308901.png)


If you want to run this app locally, you can also pull the docker image from dockerhub:
```
docker pull kaifengyu16/containerized_microservice_deploy_aws:proj2
```
And then use the following command to run:
```
docker run kaifengyu16/containerized_microservice_deploy_aws:proj2
```

## How to deploy
### build a docker image
1. build a docker image
```
docker build .
```
2. view docker image
```
docker image ls
```
### push docker image to ecr
1. create a private Amazon ECR repository
2. Use the AWS CLI to retrieve an authentication token and authenticate your Docker client to your registry.
```
aws ecr get-login-password --region _region_ | docker login --username AWS --password-stdin **aws_account_id**.dkr.ecr.**region**.amazonaws.com
```
4. 
### AWS App Runner Deploy
