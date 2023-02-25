.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

################
### Database ###
################
start-db: ## Starts PostgreSQL Database in with docker
	@docker compose --file ./database/docker-compose.yaml up -d

stop-db: ## Stop PostgreSQL Database
	@docker compose --file ./database/docker-compose.yaml down