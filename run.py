"""
    Runner for simple debug server
"""

from app import app


app.run(host="0.0.0.0", port=8082, debug=True)
