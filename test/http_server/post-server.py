from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class handler(BaseHTTPRequestHandler):
        def do_GET(self):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                message = "Hello, World! Here is a GET response"
                self.wfile.write(bytes(message, "utf8"))
        def do_POST(self):
                #self.send_response(200)
                #self.send_header('Content-type','text/html')
                #self.end_headers()
                #       
                #msg = self.rfile.read(int(self.headers.get("Content-Length")))
                #print(len(msg), msg)
                #message_out = ""
#
                #if b'335aa91a' in msg:
                #        message_out = "12959"
                #else: 
                #        message_out = "n"
                #        
                #self.wfile.write(bytes(message_out, "utf8"))

                self.send_response(200)
                self.send_header('Content-type','application/json')
                self.end_headers()

                msg = self.rfile.read(int(self.headers.get("Content-Length")))
                
                json_data = json.loads(msg.decode())

                print(json_data)

                response = {}

                if json_data["typ"] == "overeni":
                        if json_data["id"] == "1d38c91c031080":
                                response["key"] = "k"
                                response["nazev"] = "jilovaci423"
                                response["penize"] = "45321"
                        else:
                                response["key"] = "n"
                                
                elif json_data["typ"] == "akce":
                        response["key"] = "k"
                
                elif json_data["typ"] == "vratit":
                        pass #vrat akci

                print(response)
                self.wfile.write(bytes(json.dumps(response), "utf8"))


with HTTPServer(('192.168.180.52', 80), handler) as server:
    server.serve_forever()
