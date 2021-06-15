SHELL := /bin/bash
ENVSPATH ?= ~/envs/SiC-020210618

help: ## show whats in the makefile
	@egrep -h '##' $(MAKEFILE_LIST) | grep -v '@egrep' | awsk 'BEGIN {FS = "## "}; printf "\033[36m%-40s\033[0m %s\n", $$1, $$2}'

updateenvs: ## pip install and upgrade pip for the venv
	source $(ENVSPATH) && pip install --upgrade pip;
	source $(ENVSPATH) && pip install -r requirements.txt;
	echo source $(ENVSPATH)
