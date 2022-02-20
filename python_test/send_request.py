import socket
import config
from http.client import HTTPResponse

def send_request(request_header, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((config.SERVER_ADDR, port))
    client.send(request_header.encode())
    http_response = HTTPResponse(client)
    http_response.begin()
    return http_response
