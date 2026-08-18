import http.server
import socketserver
import socket
import sys

# Ensure UTF-8 output encoding for console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

PORT = 8080

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Allow cross-origin access and prevent aggressive caching
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

if __name__ == '__main__':
    local_ip = get_local_ip()
    
    # Enable address reuse so server restarts without port conflict issues
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("0.0.0.0", PORT), CustomHTTPRequestHandler) as httpd:
        print("=" * 65)
        print("GENIUS TRADERS AI SAAS WEB APP IS RUNNING!")
        print("=" * 65)
        print(f"1. Desktop PC (Localhost):        http://localhost:{PORT}")
        print(f"2. Same Wi-Fi Network Devices:    http://{local_ip}:{PORT}")
        print("3. Mobile Data / Different Wi-Fi: Run 'npx localtunnel --port 8080'")
        print("=" * 65)
        print("Press Ctrl+C to stop the server.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped successfully.")
            httpd.server_close()
