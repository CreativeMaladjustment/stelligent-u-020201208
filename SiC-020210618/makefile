SHELL := /bin/bash
ENVSPATH ?= ~/envs/SiC-020210618

help: ## show whats in the makefile
	@egrep -h '##' $(MAKEFILE_LIST) | grep -v '@egrep' | awk 'BEGIN {FS = "## "}; {printf "\033[36m%-40s\033[0m %s\n", $$1, $$2}'

createenvs: ## make the venv 
	python3 -m venv $(ENVSPATH)

updateenvs: ## pip install and upgrade pip for the venv
	source $(ENVSPATH)/bin/activate && pip install --upgrade pip;
	source $(ENVSPATH)/bin/activate && pip install -r requirements.txt;
	echo source $(ENVSPATH)/bin/activate;
# per each new package will have to do an install like
# pip install aws_cdk.aws_codecommit

freezeenvs: ## update the requirements.txt file and remove pkg-resources if in an env
	source $(ENVSPATH)/bin/activate && pip freeze | grep -v "pkg-resources" > requirements.txt

installcdk: ## onetime thing (also use npm to update cdk)
	sudo npm install -g aws-cdk;
	pip install aws_cdk.aws_codecommit aws_cdk.aws_cloud9 aws_cdk.aws_codecommit
# this assumes something like sudo apt install nodejs npm has been run

cdkinit: ## setup inital cdk application only needs to be run once
	cdk init --language python
# this also has to be done in an empty directory so move this make file up a dir and 
# make -f ../makefile cdkinit # or something

deploycodecommit: ## use cdk to deploy code commit
	cdk deploy sic-020210618-codecommit-stack --profile temp

clonesic020210618: ## clone the new repo
	git clone codecommit::us-east-1://temp@sic020210618 ~/git/sic020210618

clonesicpipeline: ## clone the new pipeline repo
	git clone codecommit::us-east-1://temp@sic-020210618-pipeline ~/git/sic-020210618-pipeline

deploycloud9: ## cdk deploy the cloud9 stack
	cdk deploy sic020210618Cloud9 --profile temp
