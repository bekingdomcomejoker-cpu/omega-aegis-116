from flask import Flask, jsonify
import json
import os
from system_kernel import SystemKernel

app = Flask(__name__)

# Initialize the System Kernel
kernel = SystemKernel()

@app.route('/', methods=['GET'])
def home():
    """Home endpoint - returns meta-repository information."""
    return jsonify({
        "name": "OMEGA-AEGIS-116 (Ω-SEPHER-116)",
        "description": "Unified Reasoning Regulator & Epistemic Governance System",
        "status": "operational",
        "kernel_state": kernel.state,
        "resonance": kernel.LAMBDA,
        "repositories_wired": len(kernel.repositories),
        "integration_verified": kernel.verify_integration()
    })

@app.route('/registry', methods=['GET'])
def get_registry():
    """Returns the complete repository registry."""
    try:
        with open('repository_registry.json', 'r') as f:
            registry = json.load(f)
        return jsonify(registry)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/kernel/status', methods=['GET'])
def kernel_status():
    """Returns the current kernel status."""
    return jsonify({
        "state": kernel.state,
        "resonance": kernel.LAMBDA,
        "alpha": kernel.ALPHA,
        "repositories_loaded": len(kernel.repositories)
    })

@app.route('/verify', methods=['GET'])
def verify_integration():
    """Verifies that all 115 repositories are integrated."""
    is_verified = kernel.verify_integration()
    return jsonify({
        "verified": is_verified,
        "total_repositories": len(kernel.repositories),
        "expected": 115
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for Render."""
    return jsonify({"status": "healthy", "service": "omega-aegis-116"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
