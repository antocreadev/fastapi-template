run-api-dev :
	uvicorn src.main:app --host 0.0.0.0 --port 7777 --reload

run-db:
	docker compose up -d

clean-db:
	docker compose down

.PHONY: run-api-dev run-db clean-db