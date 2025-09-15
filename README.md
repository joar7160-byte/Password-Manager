# Password-Manager
simple Python password manager that securely handles account creation and login using bcrypt hashing and getpass for hidden input. Demonstrates secure credential storage, authentication, and core cybersecurity practices for SOC and security-focused roles.

## ✨ Features  
- 📝 Create accounts with unique usernames  
- 🔑 Secure password hashing using **bcrypt** (with salting)  
- 🙈 Hidden password input with **getpass**  
- ✅ Login system with credential verification  
- 👋 Exit functionality with clean termination  

## 🛡️ Security Highlights  
- **No plaintext storage** – all passwords are hashed with bcrypt.  
- **Salting & cost factor** – protects against rainbow table and brute-force attacks.  
- **Authentication logic** – enforces proper credential checks before granting access.  

## 🧰 Tech Stack  
- **Python 3**  
- **bcrypt** – password hashing  
- **getpass** – secure, hidden password input  

## 🚀 Usage  
Clone the repository and install bcrypt:  
```bash
pip install bcrypt


