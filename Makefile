.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

################
### Backend ###
################
run-backend: ## Starts uvicorn server on Port 3000
	@cd ./backend && python3 -m uvicorn main:app --reload --port 3000

################
### Database ###
################
start-db: ## Starts PostgreSQL Database in with docker
	@docker compose --file ./database/docker-compose.yaml up -d

stop-db: ## Stop PostgreSQL Database
	@docker compose --file ./database/docker-compose.yaml down

################
### Frontend ###
################
run-frontend: ## Starts uvicorn server on Port 8080
	@cd ./frontend && python3 -m uvicorn main:app --reload --port 8080