import argparse
from scbcli.scanner import start_scan, get_scan_status

def main():
    parser = argparse.ArgumentParser(
        description="SecureCodeBox CLI - A tool to manage security scans in Kubernetes"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: Start a scan
    start_parser = subparsers.add_parser("start", help="Start a new scan")
    start_parser.add_argument("scanner", help="Scanner type (e.g., nmap, zap)")
    start_parser.add_argument("target", help="Target URL or IP address")
    start_parser.add_argument("-n", "--namespace", help="Kubernetes namespace", default="default")

    # Command: Check scan status
    status_parser = subparsers.add_parser("status", help="Check scan status")
    status_parser.add_argument("scan_name", help="Name of the scan")
    status_parser.add_argument("-n", "--namespace", help="Kubernetes namespace", default="default")

    args = parser.parse_args()

    if args.command == "start":
        start_scan(args.scanner, args.target, args.namespace)
    elif args.command == "status":
        get_scan_status(args.scan_name, args.namespace)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
