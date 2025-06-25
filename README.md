Vector Clock-Based Causal Key-Value Store
This project implements a distributed key-value store across multiple nodes that maintains causal consistency using Vector Clocks. Built using Python (Flask) and fully containerized with Docker Compose, the system ensures that causally dependent writes are applied in the correct order across all nodes—even in the presence of message delays or out-of-order delivery.

🔧 Features
⏱️ Vector Clock implementation to track event causality

📦 Local key-value storage per node with causal replication

🕒 Write buffering and deferred delivery until causal dependencies are met

🔄 Client simulation of reads/writes across nodes

🐳 Docker-based multi-node orchestration

📁 Directory Structure
bash
Copy
Edit
vector-clock-kv-store/
├── src/
│   ├── node.py       # Node server with vector clock logic
│   └── client.py     # Client to simulate operations
├── Dockerfile        # Container setup for each node
├── docker-compose.yml
└── project_report1.pdf

✅ Use Case
Designed as an academic assignment to demonstrate the practical application of vector clocks in distributed systems. The project validates causal consistency through controlled client scenarios and log-based verification.
