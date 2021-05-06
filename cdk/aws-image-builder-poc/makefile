SHELL := /bin/bash
ENVSPATH ?= ~/.env-aws-image-builder-poc/bin/activate

help: 
	@egrep -h '##' $(MAKEFILE_LIST) | grep -v '@egrep' | awk 'BEGIN {FS = "## "}; {printf "\033[36m%-40s\033[0m %s\n", $$1, $$2}'
	
init: ## pip updates in virtual enviroment and echo source to copy paste
	source $(ENVSPATH) && pip install --upgrade pip;
	source $(ENVSPATH) && pip install -r requirements.txt;
	echo source $(ENVSPATH);

freeze: ## update requirements text file removing pkg-resources which causes an issue
	source $(ENVSPATH) && pip freeze | grep -v "pkg-resources" > requirements.txt

cdkdiff: ## check for differences between code and the stack
	cdk diff

cdksynth: ## provide cloudformation yml from code for these changes
	cdk synth
	
cdkdeploy: ## deploy the changes
	cdk deploy
	
initvevn: ## starting in a new cloud9 or environment make the venv
	python3 -m venv ~/.env-aws-image-builder-poc

