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


testcases_other = {
    "invalid method test": f"HOGE / HTTP/1.1\r\nHost:default_server\r\n\r\n",
}


def test_other():
    for k, v in testcases_other.items():
        testcase(k, v)
