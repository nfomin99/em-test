from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Hello from Effective Mobile!"
        self.wfile.write(message.encode('utf-8'))

host = ''
port = 8080

server = HTTPServer((host, port), SimpleHandler)
print(f"Сервер запущен на http://{host}:{port}")
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
server.server_close()
print("Сервер остановлен")