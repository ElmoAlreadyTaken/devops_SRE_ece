# Devops Project - Web Application

## Introduction :
Devops project for ECE.
Group : Nassim SI MOHAMMED, Misha SETTA, Axel PAPE.
Teachers : Sergei KUDINOV & Gonzalo ETSE

Original instructions git : https://github.com/adaltas/ece-devops-2022-fall/blob/main/project/instructions.md

We've use the web_app developped in js instead of the one we've developped in python (you can found it on /userapi_py, it works) .
## Prerequisites

* Nodejs
* Npm
* Vagrant
* VirtualBox
* docker
* docker-compose (V2)
* Kubernetes (k8s)

## Getting Started

```
git clone https://github.com/ElmoAlreadyTaken/devops_SRE_ece.git
```

## Bring up the webapp in local

In one terminal :
```
cd userapi
redis-server
```

In a second terminal :
```
cd userapi
npm install
npm start
```

In a third one :
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"sergkudinov","firstname":"sergei","lastname":"kudinov"}' \
  http://localhost:3000/user
```

You should have as output :
```
{"status":"success","msg":"OK"}
```

## Bring up the Virtual Machine

```
cd iac
vagrant up
```

## Bring up docker compose

```
cd ..
cd userapi
docker-compose up
```

# Enjoy !
