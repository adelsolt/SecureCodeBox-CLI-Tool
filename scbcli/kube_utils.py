import subprocess
import json

def apply_yaml(yaml_content):
    """Apply a YAML configuration to Kubernetes using kubectl."""
    process = subprocess.run(
        ["kubectl", "apply", "-f", "-"],
        input=yaml_content,
        text=True,
        capture_output=True
    )
    if process.returncode == 0:
        print("YAML applied successfully!")
    else:
        print(f"Error applying YAML: {process.stderr}")

def get_scan_output(scan_name, namespace="default"):
    """Retrieve the scan status from Kubernetes."""
    process = subprocess.run(
        ["kubectl", "get", "scans", scan_name, "-n", namespace, "-o", "json"],
        capture_output=True,
        text=True
    )

    if process.returncode != 0:
        return f"Error fetching scan status: {process.stderr}"

    try:
        scan_data = json.loads(process.stdout)
        return scan_data.get("status", {}).get("state", "Unknown")
    except json.JSONDecodeError:
        return "Error parsing scan status response."
