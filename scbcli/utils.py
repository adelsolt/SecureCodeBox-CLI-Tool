import yaml
from scbcli.kube_utils import apply_yaml, get_scan_output

def generate_scan_yaml(scanner_name, target_url, namespace="default"):
    """Generate SecureCodeBox scan YAML dynamically."""
    scan_config = {
        "apiVersion": "execution.securecodebox.io/v1",
        "kind": "Scan",
        "metadata": {
            "name": f"{scanner_name}-scan",
            "namespace": namespace
        },
        "spec": {
            "scanType": scanner_name,
            "parameters": ["-t", target_url]
        }
    }
    return yaml.dump(scan_config, default_flow_style=False)

def start_scan(scanner_name, target_url, namespace="default"):
    """Start a new scan by applying the generated YAML."""
    yaml_content = generate_scan_yaml(scanner_name, target_url, namespace)
    apply_yaml(yaml_content)
    print(f"Scan {scanner_name} started successfully!")

def get_scan_status(scan_name, namespace="default"):
    """Retrieve and print the status of a SecureCodeBox scan."""
    status = get_scan_output(scan_name, namespace)
    print(f"Scan Status: {status}")

    if status == "COMPLETED":    
        print("Scan completed successfully!")
    elif status == "FAILED":
        print("Scan failed!")
    elif status == "IN_PROGRESS":
        print("Scan in progress...")
    elif status == "ABORTED":
        print("Scan aborted!")
    elif status == "ERROR":
        print("Scan encountered an error!")
    else:
        print("Unknown scan status")    