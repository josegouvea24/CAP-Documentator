import sys
import os

# Make sure `src` is in the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from api.main import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)