<!--
  ╔══════════════════════════════════════════════════════════════════════════════╗
  ║  POISONED QUANTUM JOB — SAFE DETECTION SCENARIO                              ║
  ║  Educational cybersecurity PoC using Qiskit                                    ║
  ╚══════════════════════════════════════════════════════════════════════════════╝
-->

<div align="center">

<!-- HEADER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1a2e,100:16213e&height=200&section=header&text=Poisoned%20Quantum%20Job%20Detector&fontSize=42&fontColor=00d4ff&animation=fadeIn&fontAlignY=35&desc=Safe%20Detection%20Scenario%20%E2%80%94%20Educational%20Cybersecurity%20PoC&descAlignY=55&descSize=15"/>

<br>

<!-- BADGES -->
<p>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Qiskit-1.0+-6929C4?style=for-the-badge&logo=ibm&logoColor=white"/>
  <img src="https://img.shields.io/badge/Qiskit_Aer-0.17+-6929C4?style=for-the-badge&logo=ibm&logoColor=white"/>
</p>

<p>
  <img src="https://img.shields.io/badge/Purpose-Educational%20PoC-blue?style=flat-square&color=0d1117"/>
  <img src="https://img.shields.io/badge/Status-Safe%20%26%20Sandboxed-success?style=flat-square&color=0d1117"/>
  <img src="https://img.shields.io/badge/License-MIT-0d1117?style=flat-square"/>
</p>

<br>

<!-- TYPING ANIMATION -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2500&pause=800&color=00D4FF&center=true&vCenter=true&width=600&lines=Circuit%20Analysis%20%F0%9F%94%8D;Security%20Gateway%20%F0%9F%9B%A1%EF%B8%8F;Resource%20Threshold%20Detection%20%E2%9A%A0%EF%B8%8F;Safe%20Local%20Execution%20%E2%9C%85" alt="Typing SVG"/>
</a>

</div>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

## ⚠️ Important Notice

> **This is an educational cybersecurity Proof-of-Concept (PoC).**
>
> This project demonstrates how to **detect** suspicious quantum jobs before execution.  
> It intentionally **DOES NOT** submit any attack to a real quantum backend.  
> All execution happens locally via `AerSimulator` only after security validation passes.

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

## 🎯 Scenario

An untrusted user submits a quantum circuit to a cloud-based quantum computing platform. The circuit may contain suspicious characteristics:

| Suspicious Indicator | Description | Risk |
|----------------------|-------------|------|
| **Excessive Depth** | Abnormally long circuit depth | Resource exhaustion, Denial of Service |
| **Too Many Operations** | Unusually high gate count | Wasted compute credits, queue starvation |
| **Excessive Two-Qubit Gates** | Too many entangling operations | Crosstalk noise, fidelity degradation |

**The security gateway analyzes the circuit before execution and blocks suspicious jobs.**

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

## 🏗️ Architecture

```
poisoned-quantum-job/
├── 📄 quantum_security_gateway.py    # Main script
├── 📄 requirements.txt               # Python dependencies
└── 📄 README.md                      # This file
```

### Module Breakdown

| Function | Purpose |
|----------|---------|
| `create_normal_job()` | Generates a benign 5-qubit circuit (Hadamard + CNOT chain) |
| `create_suspicious_job()` | Generates a resource-heavy circuit (100× repetition loop) |
| `analyze_job(qc)` | Extracts metrics: qubits, depth, operations, two-qubit gates |
| `security_gateway(qc)` | Applies thresholds and decides allow/block |
| Safe Execution | Runs `AerSimulator` **only** if validation passes |

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.10+
python --version

# Install Qiskit and Aer simulator
pip install qiskit qiskit-aer
```

### Run the Demo

```bash
# Clone or download the script
git clone https://github.com/yourusername/poisoned-quantum-job.git
cd poisoned-quantum-job

# Run the security gateway demo
python quantum_security_gateway.py
```

### Expected Output

```text

NORMAL JOB
========== QUANTUM JOB SECURITY CHECK ==========
Qubits:             5
Circuit depth:      6
Operations:         14
Two-qubit gates:    4

[+] Job passed security validation.


SUSPICIOUS / POISONED JOB
========== QUANTUM JOB SECURITY CHECK ==========
Qubits:             5
Circuit depth:      601
Operations:         900
Two-qubit gates:    400

[!] SUSPICIOUS JOB DETECTED
    - Abnormally high circuit depth
    - Excessive operation count
    - Excessive two-qubit gate usage

Job blocked by security gateway.

Normal job executed locally.
{'00000': 523, '00001': 48, '00010': 45, ...}
```

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

## 🔍 Security Policies

The gateway enforces these thresholds:

| Metric | Threshold | Rationale |
|--------|-----------|-----------|
| **Circuit Depth** | `> 200` | Prevents deep circuits that hog quantum hardware |
| **Operation Count** | `> 500` | Limits total gate count to control runtime |
| **Two-Qubit Gates** | `> 200` | Restricts entangling operations (noisiest gates) |

> 💡 **Customize thresholds** by editing the `analyze_job()` function:
> ```python
> if stats["depth"] > YOUR_CUSTOM_LIMIT:
>     warnings.append("...")
> ```

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

## 📋 Code Reference

### `create_normal_job()`

```python
def create_normal_job():
    qc = QuantumCircuit(5, 5)
    qc.h(range(5))           # Superposition on all qubits
    for i in range(4):
        qc.cx(i, i + 1)      # Linear entanglement chain
    qc.measure(range(5), range(5))
    return qc
```
**Metrics:** 5 qubits | Depth: 6 | Operations: 14 | CNOTs: 4

---

### `create_suspicious_job()`

```python
def create_suspicious_job():
    qc = QuantumCircuit(5, 5)
    for _ in range(100):     # 100× repetition — abnormal!
        for q in range(5):
            qc.h(q)
        for q in range(4):
            qc.cx(q, q + 1)
    qc.measure(range(5), range(5))
    return qc
```
**Metrics:** 5 qubits | Depth: 601 | Operations: 900 | CNOTs: 400

---

### `analyze_job(qc)`

```python
def analyze_job(qc):
    stats = {
        "qubits": qc.num_qubits,
        "depth": qc.depth(),
        "operations": qc.size(),
        "two_qubit_gates": 0,
    }
    for instruction in qc.data:
        operation = instruction.operation
        if operation.num_qubits >= 2:
            stats["two_qubit_gates"] += 1
    # ... threshold checks ...
    return stats, warnings
```

---

### `security_gateway(qc)`

```python
def security_gateway(qc):
    stats, warnings = analyze_job(qc)
    # Print metrics
    # If warnings: print alerts → return False (BLOCK)
    # Else: return True (ALLOW)
```

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

## 🛡️ Safety Guarantees

| Guarantee | Implementation |
|-----------|---------------|
| **No real backend submission** | Uses `AerSimulator` only |
| **Validation before execution** | Gateway runs before any `backend.run()` |
| **Blocked jobs never execute** | `return False` prevents further processing |
| **Local-only simulation** | No cloud API keys or remote calls |

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

## 🔧 Extending the Gateway

Add new detection rules:

```python
def analyze_job(qc):
    stats, warnings = base_analysis(qc)

    # New: detect unauthorized gate types
    forbidden_gates = {"reset", "delay", "initialize"}
    for instruction in qc.data:
        if instruction.operation.name in forbidden_gates:
            warnings.append(f"Forbidden gate: {instruction.operation.name}")

    # New: detect measurement tampering
    if qc.num_clbits != qc.num_qubits:
        warnings.append("Mismatched qubit/classical bit count")

    return stats, warnings
```

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

## 📚 Requirements

```text
qiskit>=1.0
qiskit-aer>=0.17
```

Install via:
```bash
pip install -r requirements.txt
```

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

## 📜 License

MIT License — See [LICENSE](LICENSE) for details.

> **Educational Use Only.** This code is designed for learning about quantum security concepts in a safe, sandboxed environment.

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:16213e,50:1a1a2e,100:0d1117&height=120&section=footer&text=Stay%20Safe%20%E2%9A%9B%EF%B8%8F%20Research%20Responsibly&fontSize=24&fontColor=00d4ff&animation=fadeIn"/>

</div>
