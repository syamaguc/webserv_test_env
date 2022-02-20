from send_request import send_request
import config


def testcase(description, nginx_request_header, webserv_request_header):
    print(description.ljust(42), end=": ")
    try:
        http_response_nginx = send_request(
            nginx_request_header, config.NGINX_CGI_SERVER_PORT)
    except:
        print("ERROR -> nginx")
        return
    try:
        http_response_webserv = send_request(
            webserv_request_header, config.WEVSERV_CGI_SERVER_PORT)
    except:
        print("ERROR -> webserv")
        return
    if http_response_nginx.status == http_response_webserv.status:
        print("OK")
    else:
        print('NG nginx status: {}, webserv status: {}'.format(
            str(http_response_nginx.status), str(http_response_webserv.status)))


testcases_post = {
    "normal POST test": [f"POST '/cgi-bin/test_post.py?name=syamaguc' HTTP/1.1\r\n\r\nThis is POST test", f"POST '/cgi/test_post.py?name=syamaguc' HTTP/1.1\r\n\r\nThis is POST test"],
    "empty query string value POST test": [f"POST '/cgi-bin/test_post.py?name=' HTTP/1.1\r\n\r\nThis is POST test", f"POST '/cgi/test_post.py?name=' HTTP/1.1\r\n\r\nThis is POST test"],
    "empty query string POST test": [f"POST '/cgi-bin/test_post.py' HTTP/1.1\r\n\r\nThis is POST test", f"POST '/cgi/test_post.py' HTTP/1.1\r\n\r\nThis is POST test"],
    "long query": [f"POST '/cgi-bin/test_post.py?{'hoge' * 1000}={'fuga' * 1000}' HTTP/1.1\r\n\r\nThis is POST test", f"POST '/cgi/test_post.py?{'hoge' * 1000}={'fuga' * 1000}' HTTP/1.1\r\n\r\nThis is POST test"],
}


def test_post():
    for k, v in testcases_post.items():
        testcase(k, v[0], v[1])
