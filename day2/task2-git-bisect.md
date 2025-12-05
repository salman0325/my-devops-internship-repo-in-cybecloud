
# Redmi Git Bisect Guide

This guide shows how to find a commit that introduced a bug in a repository with Git.

## 1. Start Bisect

```bash
# Start git bisect
git bisect start
```

## 2. Mark the Bad Commit

```bash
# Mark the current commit (HEAD) as bad
git bisect bad
```

> **Note:** This is the commit where the bug exists (for example, the latest commit).

## 3. Mark a Known Good Commit

```bash
# Mark an older commit as good
git bisect good HEAD~2
```

> **Explanation:** `HEAD~2` is two commits before the current commit. Git now knows the bug was not present there.

## 4. Test the Commit

Git will now check out the commit in the middle of the range (usually commit 2 in a 3-commit range).
Test this commit to see if the bug is present.

```bash
# Run your tests or check for the bug manually
# Example test command:
npm test
# or
./run_redmi_test.sh
```

## 5. Mark the Tested Commit

After testing:

```bash
# If the bug is present
git bisect bad

# If the bug is NOT present
git bisect good
```

Git will automatically check out the next commit to test, narrowing down the bad commit.

## 6. Repeat Testing

Keep testing and marking commits as `good` or `bad` until Git finds the **first bad commit**.

## 7. Finish Bisect

Once the first bad commit is found:

```bash
git bisect reset
```

> This returns you to your original branch.

## ✅ Example Flow for 3 Commits

| Commit | Status        |
| ------ | ------------- |
| 1      | good          |
| 2      | ? (test this) |
| 3      | bad           |

* Git will first test commit 2.
* Mark it `good` or `bad`.
* Git then tells you which commit introduced the bug.

