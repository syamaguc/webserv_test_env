from send_request import send_request
import config


def setup():
    send_request("PUT /upload/test.txt HTTP/1.1\r\n\r\nhogehoge",
                 config.NGINX_SERVER_PORT)
    r = send_request("POST /upload/ HTTP/1.1\r\n\r\nhogehoge",
                     config.WEVSERV_SERVER_PORT)
    return r.headers["Location"].split("/")[-1]


def testcase(description, nginx_request_header, webserv_request_header):
    create_filename = setup()
    webserv_request_header = webserv_request_header.replace(
        "FILENAME", create_filename)
    print(description.ljust(42), end=": ")
    try:
        http_response_nginx = send_request(
            nginx_request_header, config.NGINX_SERVER_PORT)
    except:
        print("ERROR -> nginx")
        return
    try:
        http_response_webserv = send_request(
            webserv_request_header, config.WEVSERV_SERVER_PORT)
    except:
        print("ERROR -> webserv")
        return
    if http_response_nginx.status == http_response_webserv.status:
        print("OK")
    else:
        print('NG nginx status: {}, webserv status: {}'.format(
            str(http_response_nginx.status), str(http_response_webserv.status)))


testcases_delete = {
    "normal DELETE test": [f"DELETE '/upload/test.txt' HTTP/1.1\r\n\r\n", f"DELETE '/upload/FILENAME' HTTP/1.1\r\n\r\n"],
    "not exist filename DELETE test": [f"DELETE '/upload/notexist.txt' HTTP/1.1\r\n\r\n", f"DELETE '/upload/notexist.txt' HTTP/1.1\r\n\r\n"],
    "invalid method DELETE test": [f"DELETE '/index.html' HTTP/1.1\r\n\r\n", f"DELETE '/upload/index.html' HTTP/1.1\r\n\r\n"],
    "invalid method DELETE test": [f"DELETE '/default_server.html' HTTP/1.1\r\n\r\n", f"DELETE '/index.html' HTTP/1.1\r\n\r\n"],
}


def test_delete():
    for k, v in testcases_delete.items():
        testcase(k, v[0], v[1])
