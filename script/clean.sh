ID=$(docker ps | grep -e webserv_test -e nginx_test | awk '{print $1}')

docker stop $ID
docker rmi webserv_test
docker rmi nginx_test
