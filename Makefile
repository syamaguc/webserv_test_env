setup:
	@rm -rf webserv
	@git clone git@github.com:syamaguc/webserv.git

build:
	@docker build -t nginx_test . -f Dockerfile_nginx
	@docker build -t webserv_test . -f Dockerfile_webserv

run:
	@docker run --rm -it -p 50000:50000 -p 50001:50001 -p 50002:50002 -d --name nginx_test_env   nginx_test
	@docker run --rm -it -p 8080:8080 	-p 8081:8081 	-p 8888:8888  -d --name webserv_test_env webserv_test

docker-clean:
	@bash ./script/clean.sh

re: setup docker-clean build run
	@echo "setup test env"

exec_nginx:
	@bash ./script/exec.sh nginx_test

exec_webserv:
	@bash ./script/exec.sh webserv_test

log:
	@bash ./script/log.sh

# Configuration

## look for the HTTP response status codes list an internet and during this evaluation if any status codes is wrong don't give related points.

## setup multiple servers with different port.
test_multi_server:
	echo -e "\n\e[31m --->> port 8080 \e[m\n"
	@curl localhost:8080
	echo -e "\n\e[31m --->> port 8888 \e[m\n"
	@curl localhost:8888

## setup default error page (try to change the error 404)
## Please check sample.conf

## setup multiple servers with different hostname.
test_virtual_server:
	echo -e "\n\e[31m --->> default_server (port 8080)\e[m\n"
	@curl -H 'Host:default_server' localhost:8080
	echo -e "\n\e[31m --->> virtual_server (port 8080)\e[m\n"
	@curl -H 'Host:virtual_server' localhost:8080

## limit the client body
test_limit_client_body:
	@curl -X POST --data "`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 16 | head -n 3000 | sort | uniq`" localhost:8080/upload/

## setup routes in a server to directories
## setup a default file to search for if you ask for a directory
## setup a list of method accepted for a certain route (ex, try to delete something with and without permission)
test_invalid_method:
	@echo -e "\n\e[31m --->> POST request\e[m\n"
	@curl -X POST --data "This is test POST request" localhost:8080/
	@echo -e "\n\e[31m --->> DELETE request\e[m\n"
	@curl -X DELETE  localhost:8080/default_server.html

# Basic checks
## GET request
test_get:
	@python3 -B python_test/main.py get

## POST request
test_post:
	@python3 -B python_test/main.py post

## DELETE request
test_delete:
	@python3 -B python_test/main.py delete

## other request
test_other:
	@python3 -B python_test/main.py other

## Stress test
test_siege:
	@bash ./script/siege.sh
