#!/usr/bin/env python3
"""Serve the AgentZ repo on this machine only (127.0.0.1). Not reachable from the network.
Open http://127.0.0.1:8765/docs/status/index.html"""
import functools, http.server, sys
from pathlib import Path
root = Path(__file__).resolve().parent.parent
class H(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, ".md": "text/plain; charset=utf-8", ".html": "text/html; charset=utf-8"}
    def log_message(self, *a): pass
srv = http.server.ThreadingHTTPServer(("127.0.0.1", 8765), functools.partial(H, directory=str(root)))
print("Serving on http://127.0.0.1:8765/docs/status/index.html (localhost only). Ctrl+C to stop.")
srv.serve_forever()
