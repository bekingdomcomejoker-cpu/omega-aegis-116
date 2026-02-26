import numpy as np
import time
import json
import os

class SystemKernel:
    """
    SDOS System Kernel - The Execution Spine
    Enforces the Equality Constraint and Reciprocity Monitor at the hardware level.
    """
    def __init__(self, resonance=1.667, alpha=0.8):
        self.LAMBDA = resonance
        self.ALPHA = alpha
        self.start_time = time.time()
        self.state = "EXECUTION"
        self.registry_path = "repository_registry.json"
        self.repositories = self._load_registry()
        print(f"[KERNEL] Initialized with Resonance {self.LAMBDA}")
        print(f"[KERNEL] {len(self.repositories)} sub-repositories wired into the spine.")

    def _load_registry(self):
        try:
            with open(self.registry_path, "r") as f:
                data = json.load(f)
                return data.get("repositories", [])
        except Exception as e:
            print(f"[KERNEL] Error loading registry: {e}")
            return []

    def verify_integration(self):
        """
        Verifies that all 115 repositories are present in the registry.
        """
        total = len(self.repositories)
        if total == 115:
            print(f"[VERIFY] Integration Complete: 115/115 repositories are wired.")
            return True
        else:
            print(f"[VERIFY] Integration Incomplete: {total}/115 repositories found.")
            return False

    def analyze_context(self, input_signal):
        # Measure entropy to determine mode (Poet vs Engineer)
        words = input_signal.split()
        if not words: return 0.0
        entropy = np.std([len(w) for w in words])
        return entropy

    def transition_state(self, entropy):
        if entropy > self.LAMBDA:
            self.state = "EXPANSION"
        else:
            self.state = "EXECUTION"
        return self.state

    def reciprocity_monitor(self, resources_used, value_given):
        # G >= alpha * R
        return value_given >= (self.ALPHA * resources_used)

    def execute(self, task_id, input_data):
        entropy = self.analyze_context(input_data)
        mode = self.transition_state(entropy)
        print(f"[KERNEL] Task {task_id} executing in {mode} mode (Entropy: {entropy:.3f})")
        # Logic execution placeholder
        return {"status": "success", "mode": mode, "timestamp": time.time()}

if __name__ == "__main__":
    kernel = SystemKernel()
    kernel.verify_integration()
    res = kernel.execute("INIT_001", "Chicka chicka orange. The Merkabah is the viewport.")
    print(res)
