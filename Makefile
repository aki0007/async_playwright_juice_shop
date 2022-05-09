.PHONY: allure-serve,compose-build,compose-test,compose-test-allure
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


ALLURE_DIR := reports/allure-results
COMPOSE_SVC_NAME := playwright-demo


help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

allure-serve: ## test
	@allure serve $(ALLURE_DIR)

compose-build: ## build the docker-compose service
	@docker-compose build

compose-test: ## test
	@docker-compose run $(COMPOSE_SVC_NAME) pytest -s -v tests/juice_shop.py $(args)

compose-test-allure: ## test
	@docker-compose run $(COMPOSE_SVC_NAME) pytest -s -v tests/juice_shop.py --alluredir=$(ALLURE_DIR) $(args)
	@make allure-serve
