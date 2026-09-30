from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import urllib.parse
import sqlworker

class LogHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = urllib.parse.parse_qs(post_data)
        session_id = parsed_data.get('session', [''])[0]
        pfsense_ip = parsed_data.get('pfsense_ip2', [''])[0]
        client_ip = self.client_address[0]
        
        if session_id:
            print("Session ID Received")
            sqlworker.insert(client_ip, pfsense_ip, session_id)
            print(pfsense_ip)
            self.send_response(200)
            self.end_headers()
        else:
            self.send_error(400, "Bad Request: Missing session ID")

def main():
    print("Starting Server")
    ThreadingHTTPServer(('', 7777), LogHandler).serve_forever()

if __name__ == "__main__":
    main()