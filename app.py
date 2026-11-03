import json
import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", "5432"))


def db_ok():
    try:
        socket.create_connection((DB_HOST, DB_PORT), timeout=2).close()
        return True
    except OSError as e:
        print(f"ERREUR connexion base {DB_HOST}:{DB_PORT} -> {e}", flush=True)
        return False


class Handler(BaseHTTPRequestHandler):
    def send_json(self, code, body):
        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/health":
            if db_ok():
                self.send_json(200, {"status": "ok", "db": "up"})
            else:
                self.send_json(503, {"status": "error", "db": "down"})
        elif self.path == "/info":
            self.send_json(200, {"app": "campus-tasks", "db_host": DB_HOST, "db_port": DB_PORT})
        else:
            self.send_json(404, {"error": "not found"})


if __name__ == "__main__":
    print("Campus Tasks ecoute sur 0.0.0.0:8080", flush=True)
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
