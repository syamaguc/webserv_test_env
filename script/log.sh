docker exec `docker ps | grep webserv_test | awk '{print $1}'` tail -f /var/log/nginx/error.log
