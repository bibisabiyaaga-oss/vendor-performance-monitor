from flask import Flask
from routes.describe import describe_bp

app = Flask(__name__)

# Register describe route
app.register_blueprint(describe_bp)

# Health check route
@app.route('/health', methods=['GET'])
def health():
    return {"status": "ok", "service": "ai-service"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)