sed -i 's/%AUTO_INDEX%/'$NGINX_AUTO_INDEX'/g' $NGINX_SITES_DIR/default
cat $NGINX_SITES_DIR/default
#kill -9 $(lsof -i | grep nginx | awk '{print $2}')
#service nginx restart
service fcgiwrap restart
nginx -t
nginx -g 'daemon off;'
