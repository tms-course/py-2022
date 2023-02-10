INFRA_DIR=$(shell pwd)

.PHONY=build
build:
	cd $(INFRA_DIR)/todos-react && npm run build
	cp -r $(INFRA_DIR)/todos-react/build $(INFRA_DIR)/todo_project/static/