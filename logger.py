from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class LogHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        session_id = urllib.parse.parse_qs(post_data).get('session', [''])[0]
        
        if session_id:
            with open("pfsense_master_log.txt", "a") as log:
                log.write(f"Session ID: {session_id}\n")
                
            self.send_response(200)
            self.end_headers()

# Starts a quiet local server
HTTPServer(('localhost', 8000), LogHandler).serve_forever()