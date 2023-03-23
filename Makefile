include .env
.PHONY: allure-serve,compose-build,pull,playwright-codegen,test,test-allure,test-testrail,testrail-creds,
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


ALLURE_DIR := report/allure-report
COMPOSE_SVC_NAME := async_playwright

# Jenkins file parameters
pytestOPT ?=

export TR_TESTRUN_NAME := "Automated testrun $(ENVIRONMENT) $(BROWSER) $(LOGIN_USERNAME) $(shell date --iso=seconds)"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

allure-serve: ## test
	@allure serve $(ALLURE_DIR)

compose-build: ## build the docker-compose service
	@docker-compose build

pull:
	@docker-compose pull

playwright-codegen:
	@make pull
	@docker-compose up -d && sleep 3 && playwright codegen http://localhost:3000 && docker-compose stop

test: ## test
	pytest -s -v $(args)

test-allure: ## test
	-pytest -s -v --alluredir=$(ALLURE_DIR) $(args)
	@make allure-serve

test-testrail: ## test
	@make testrail-creds
	-pytest -s -v --testrail --tr-config=testrail.cfg --alluredir=$(ALLURE_DIR) --tr-testrun-name=$(TR_TESTRUN_NAME) $(args)
	@make allure-serve

testrail-creds: ## test
	@docker-compose run $(COMPOSE_SVC_NAME) python3.11 creds.py
