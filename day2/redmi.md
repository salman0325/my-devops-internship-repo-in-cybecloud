
# 🔐 Git Commit Signing (GPG) + SSH Push Setup (Ubuntu)

This guide explains how to set up **GPG-signed commits** and **SSH-based push** on Ubuntu step-by-step.

---

## 🪜 1. Install Required Tools

```bash
sudo apt update
sudo apt install git gnupg openssh-client -y
````

---

## 🔑 2. Generate a GPG Key

```bash
gpg --full-generate-key
```

When asked:

| Question     | Answer                |
| ------------ | --------------------- |
| Key type     | RSA and RSA           |
| Key size     | 4096                  |
| Expire       | 1y                    |
| Name & Email | Use same as Git       |
| Passphrase   | (Choose a strong one) |

List your key:

```bash
gpg --list-secret-keys --keyid-format=long
```

Copy your **GPG key ID**, e.g. `ABC123DEF456`.

---

## ⚙️ 3. Configure Git to Use the Key

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global user.signingkey ABC123DEF456
git config --global commit.gpgsign true
```

Tell GPG which terminal to use:

```bash
echo 'export GPG_TTY=$(tty)' >> ~/.bashrc
source ~/.bashrc
```

---

## 📤 4. Add Your GPG Key to GitHub

Export your **public key**:

```bash
gpg --armor --export you@example.com
```

Copy everything starting from:

```
-----BEGIN PGP PUBLIC KEY BLOCK-----
...
-----END PGP PUBLIC KEY BLOCK-----
```

Then go to:
**GitHub → Settings → SSH and GPG keys → New GPG key**
Paste it and click **Add GPG key** ✅

---

## 🧪 5. Test Commit Signing

Inside your repository:

```bash
git add .
git commit -S -m "Test signed commit"
```

You’ll be asked for your GPG passphrase (once).
Verify signature:

```bash
git log --show-signature
```

You should see:

```
gpg: Good signature from "Your Name <you@example.com>"
```

---

## 🔐 6. Set Up SSH for GitHub (Push Without Password)

### Step 1: Generate SSH Key

```bash
ssh-keygen -t ed25519 -C "you@example.com"
```

(Press **Enter** for file name and optionally add a passphrase.)

### Step 2: Start SSH Agent and Add the Key

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### Step 3: Add SSH Key to GitHub

Show your public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the line (starts with `ssh-ed25519`)
→ Go to **GitHub → Settings → SSH and GPG keys → New SSH key**
Paste and click **Add SSH key** ✅

### Step 4: Test Connection

```bash
ssh -T git@github.com
```

Expected message:

```
Hi yourusername! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## 🚀 7. Change Repo Remote to SSH

Switch from HTTPS to SSH:

```bash
git remote set-url origin git@github.com:yourusername/your-repo.git
```

Check:

```bash
git remote -v
```

You should see:

```
origin  git@github.com:yourusername/your-repo.git (fetch)
origin  git@github.com:yourusername/your-repo.git (push)
```

---

## 🧩 8. Push Signed Commits via SSH

```bash
git push -u origin main
```

You’ll see output like:

```
To github.com:yourusername/your-repo.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

Go to your repository — your commit should show a **“Verified”** badge ✅

---

## ✅ Done!

You now have:

* GPG-signed commits for identity verification
* SSH authentication for secure pushing
* Fully automated signing and passwordless pushing

---

**Author:** *SALMAN KHAN*
**Platform:** Ubuntu Linux


