from send_request import send_request
import config


def testcase(description, request_header):
    print(description.ljust(42), end=": ")
    try:
        http_response_nginx = send_request(
            request_header, config.NGINX_SERVER_PORT)
    except:
        print("ERROR -> nginx")
        return
    try:
        http_response_webserv = send_request(
            request_header, config.WEVSERV_SERVER_PORT)
    except:
        print("ERROR -> webserv")
        return
    if http_response_nginx.status == http_response_webserv.status:
        print("OK")
    else:
        print('NG nginx status: {}, webserv status: {}'.format(
            str(http_response_nginx.status), str(http_response_webserv.status)))


testcases_get = {
    "normal GET test": f"GET / HTTP/1.1\r\nHost:default_server\r\n\r\n{config.SERVER_ADDR}",
    "invalid uri": f"GET /hogehoge/fugafuga HTTP/1.1\r\nHost:default_server\r\n\r\n{config.SERVER_ADDR}",
    # "multiple host": f"GET / HTTP/1.1\r\nHost:hoge\r\nHost:fuga\r\n\r\n{config.SERVER_ADDR}",
    "invalid host": f"GET / HTTP/1.1\r\nHost:hogehoge_server\r\n\r\n{config.SERVER_ADDR}",
    # "normal content length (100)": f"GET / HTTP/1.1\r\nContent-Length: 10000\r\n\r\n{config.SERVER_ADDR}",
    "invalid content length (-1)": f"GET / HTTP/1.1\r\nContent-Length: -1\r\n\r\n{config.SERVER_ADDR}",
    "invalid content length (not digit)": f"GET / HTTP/1.1\r\nContent-Length: hogehoge\r\n\r\n{config.SERVER_ADDR}",
    # "long content length (100000000000)": f"GET / HTTP/1.1\r\nContent-Length: 100000000000\r\n\r\n{config.SERVER_ADDR}",
    "content length with Transfer-Encoding": f"GET / HTTP/1.1\r\nContent-Length: 10000\r\nTransfer-Encoding: chunked\r\n\r\n{config.SERVER_ADDR}",
    "multiple content length": f"GET / HTTP/1.1\r\nContent-Length: 10\r\nContent-Length: 100\r\n\r\n{config.SERVER_ADDR}",
    "space between Host name": f"GET / HTTP/1.1\r\nHost : default_server\r\n\r\n{config.SERVER_ADDR}",
    "space before method": f" GET / HTTP/1.1\r\nHost:default_server\r\n\r\n{config.SERVER_ADDR}",
    "invalid Accept-Language": f"GET / HTTP/1.1\r\nHost:default_server\r\nAccept-Language: hogehoge\r\n\r\n{config.SERVER_ADDR}",
    "undefined header name": f"GET / HTTP/1.1\r\nHost:default_server\r\n:undefined\r\n\r\n{config.SERVER_ADDR}",
    "http_version not supported": f"GET / HTTP/4.2\r\nHost:default_server\r\n\r\n{config.SERVER_ADDR}",
    "too long URI": f"GET /{'hoge' * 40000} HTTP/1.1\r\nHost:default_server\r\n\r\n{config.SERVER_ADDR}",
}


def test_get():
    for k, v in testcases_get.items():
        testcase(k, v)
