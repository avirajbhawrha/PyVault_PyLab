# Git commands and usage

Run these commands in PowerShell or a terminal. Replace values in `<angle brackets>` with your own values; do not type the angle brackets.

## 1. Open this project folder

In PowerShell, use quotes because the parent directory contains a space:

```powershell
cd "C:\Users\avira\OneDrive\Desktop\AI samrat\project\PyVault_PyLab"
```

Check that you are in the correct folder:

```powershell
Get-Location
Get-ChildItem
```

If the project is in a different location, replace the path above with that folder's full path.

## 2. Start Git and check the repository

Initialize Git in the current project folder (only do this if it is not already a Git repository):

```powershell
git init
```

Useful checks:

```powershell
git status
git status --short
git rev-parse --show-toplevel
```

## 3. Set your author name and email

Set these once for all repositories on this computer. Use the name and email associated with your Git hosting account if applicable:

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

View the current settings:

```powershell
git config --global --list
```

To set a name or email for only this repository, omit `--global`.

## 4. Stage and save changes

Review changes, stage files, and create a commit:

```powershell
git status
git add task_day_1.py
git add .
git diff
git diff --staged
git commit -m "Describe the change"
```

`git add .` stages all changes under the current folder. Prefer `git add <file>` when you only want to stage selected files. `git diff` shows unstaged changes; `git diff --staged` shows staged changes.

Unstage a file without deleting its changes:

```powershell
git restore --staged <file>
```

Discard unstaged changes in a file (this cannot be easily undone):

```powershell
git restore <file>
```

## 5. Connect to a remote repository

Add the URL of a repository you own or have permission to use:

```powershell
git remote add origin <repository-url>
git remote -v
```

For example, the URL usually looks like `https://github.com/username/repository.git`. If `origin` is already configured, update it instead:

```powershell
git remote set-url origin <repository-url>
```

## 6. Push and pull

For the first push of the `main` branch:

```powershell
git branch -M main
git push -u origin main
```

For later pushes and updates:

```powershell
git pull
git push
```

To pull a specific branch:

```powershell
git pull origin <branch-name>
```

## 7. Branches

Create and switch to a new branch, list branches, and switch branches:

```powershell
git branch
git switch -c <new-branch>
git switch <branch-name>
```

Publish a new branch:

```powershell
git push -u origin <branch-name>
```

Merge another branch into the branch you are currently on:

```powershell
git merge <branch-name>
```

## 8. View history and compare changes

```powershell
git log --oneline
git log --oneline --graph --decorate --all
git show <commit-id>
git diff
git diff <branch-name>
```

## 9. Clone an existing repository

To download a remote repository into a new folder:

```powershell
git clone <repository-url>
```

To choose the destination folder name:

```powershell
git clone <repository-url> <folder-name>
cd <folder-name>
```

## 10. Rename and remove tracked files

Use Git commands so the rename or removal is recorded:

```powershell
git mv <old-name> <new-name>
git rm <file>
```

Then commit the change as usual. `git rm` removes the file from the working folder as well as staging its removal.

## Typical daily workflow

After the remote is configured, run these from the project folder:

```powershell
git pull
git status
git add <file>
git diff --staged
git commit -m "Describe the change"
git push
```
