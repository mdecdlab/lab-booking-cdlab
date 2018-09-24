import os
import subprocess
import threading
import http.server, ssl

def domake():
    # build directory
    #os.chdir("./../")
    server_address = ('localhost', 9444)
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                   server_side=True,
                                   certfile='./../keys/localhost.crt',
                                   keyfile='./../keys/localhost.key',
                                   ssl_version=ssl.PROTOCOL_TLSv1)
    print(os.getcwd())
    print("9444 https server started")
    httpd.serve_forever()

# 利用執行緒執行 https 伺服器
make = threading.Thread(target=domake)
make.start()