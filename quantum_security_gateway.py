
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# ---------------------------------------------------------
# 1. Create a normal quantum job
# ---------------------------------------------------------
def create_normal_job():
    qc = QuantumCircuit(5, 5)
    qc.h(range(5))
    for i in range(4):
        qc.cx(i, i + 1)
    qc.measure(range(5), range(5))
    return qc

# ---------------------------------------------------------
# 2. Create a suspicious / "poisoned" job
# ---------------------------------------------------------
def create_suspicious_job():
    qc = QuantumCircuit(5, 5)
    for _ in range(100):
        for q in range(5):
            qc.h(q)
        for q in range(4):
            qc.cx(q, q + 1)
    qc.measure(range(5), range(5))
    return qc

# ---------------------------------------------------------
# 3. Security analysis
# ---------------------------------------------------------
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

    warnings = []
    if stats["depth"] > 200:
        warnings.append("Abnormally high circuit depth")
    if stats["operations"] > 500:
        warnings.append("Excessive operation count")
    if stats["two_qubit_gates"] > 200:
        warnings.append("Excessive two-qubit gate usage")

    return stats, warnings

# ---------------------------------------------------------
# 4. Security gateway
# ---------------------------------------------------------
def security_gateway(qc):
    stats, warnings = analyze_job(qc)
    print("\n========== QUANTUM JOB SECURITY CHECK ==========")
    print(f"Qubits:             {stats['qubits']}")
    print(f"Circuit depth:      {stats['depth']}")
    print(f"Operations:         {stats['operations']}")
    print(f"Two-qubit gates:    {stats['two_qubit_gates']}")

    if warnings:
        print("\n[!] SUSPICIOUS JOB DETECTED")
        for warning in warnings:
            print(f"    - {warning}")
        print("\nJob blocked by security gateway.")
        return False

    print("\n[+] Job passed security validation.")
    return True

# ---------------------------------------------------------
# 5. Test the system
# ---------------------------------------------------------
normal_job = create_normal_job()
suspicious_job = create_suspicious_job()

print("\n\nNORMAL JOB")
gateway_result_normal = security_gateway(normal_job)

print("\n\nSUSPICIOUS / POISONED JOB")
gateway_result_suspicious = security_gateway(suspicious_job)

# ---------------------------------------------------------
# 6. Optional: execute ONLY the safe job locally
# ---------------------------------------------------------
backend = AerSimulator()

if gateway_result_normal:
    compiled = transpile(normal_job, backend)
    result = backend.run(compiled, shots=1024).result()
    print("\nNormal job executed locally.")
    print(result.get_counts())