# **scbcli - SecureCodeBox CLI Tool**

`scbcli` is a command-line tool designed to simplify SecureCodeBox scan management in Kubernetes. It allows you to start and monitor scans without manually handling YAML files configuration and without interracting with `Kubectl`

---

## **🚀 Features**
- Start SecureCodeBox scans with a single command.
- Monitor scan statuses easily.
- Automates YAML generation and Kubernetes interactions.
- Provides built-in help (`scbcli --help`) and a man page (`man scbcli`).

---

## **📌 Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/adelsolt/scbcli.git
cd scbcli
```

### **2. Install the Tool Locally**
```bash
pip install --editable .
```
This allows you to use `scbcli` from anywhere on your system.

### **3. Verify Installation**
```bash
scbcli --help
```
If installed correctly, you should see the available commands.

---

## **📌 Usage**

### **1. Start a Scan**
```bash
scbcli start <scanner> <target> [-n namespace]
```
Example:
```bash
scbcli start nmap http://example.com
```
This starts an `nmap` scan on `http://example.com` in the default Kubernetes namespace.

### **2. Check Scan Status**
```bash
scbcli status <scan_name> [-n namespace]
```
Example:
```bash
scbcli status nmap-scan
```
This checks the status of the `nmap-scan` in Kubernetes.

---

## **📌 Setting Up the Man Page**
If you want to use `man scbcli` for documentation:
```bash
sudo mv man/scbcli.1 /usr/share/man/man1/
sudo mandb
```
Now you can view the manual using:
```bash
man scbcli
```

---

## **📌 Publishing to PyPI**

### **1. Build the Package**
```bash
pip install --upgrade build
twine upload dist/*
```

### **2. Install from PyPI**
Once published, anyone can install it using:
```bash
pip install scbcli
```

---

## **📌 Uninstalling**
If you want to remove `scbcli`, run:
```bash
pip uninstall scbcli
```

---

## **📌 Contributing**
We welcome contributions! Feel free to open issues and submit pull requests.

---

## **📌 License**
This project is licensed under the MIT License.

---

## **📌 Author**
Company **KubeNoOps**
Developed by **Adel Soltane**.

GitHub: [adelsolt](https://github.com/adelsolt)

