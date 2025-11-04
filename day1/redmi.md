## **Step 1: Create Repository**

1. Go to GitHub → click **New repository**
2. Name your repository (e.g., `my-repo`)
3. Initialize with a **README** (optional)
4. Click **Create repository**

---

## **Step 2: Create Branches**

1. Clone your repo locally:

```bash
git clone https://github.com/<username>/<repo>.git
cd <repo>
```

2. Create `develop` branch:

```bash
git checkout -b develop
git push origin develop
```

3. Make sure `main` branch exists (GitHub usually creates it by default).

---

## **Step 3: Enable Branch Protection Rules**

1. Go to **Settings → Branches → Branch protection rules**

2. Click **Add rule**

3. **For `main` branch**:

   * Branch name: `main`
   * Check **Require a pull request before merging**
   * Set **Require approvals**: `1`
   * Check **Require status checks to pass before merging**

     * Select the mandatory CI/CD checks (e.g., `build`, `test`)
   * Optional: check **Include administrators**
   * Save

4. Repeat the same steps for `develop` branch

---

## **Step 4: Test the Rules**

1. Create a new branch and make a change:

```bash
git checkout -b feature/test-change
echo "test" >> test.txt
git add test.txt
git commit -m "Test change"
git push origin feature/test-change
```

2. Open a **Pull Request** to `develop` or `main`
3. Check that:

   * The **merge button is disabled** without 1 approval
   * **Mandatory checks run** before allowing merge
4. Add 1 approval and ensure the merge works

---



