# Git and Version Control Guide: Mastering Branches, Workflows, and Best Practices

Git is the industry-standard distributed version control system that tracks code changes, enables collaboration, and provides safety through branching and rollback capabilities. Understanding Git deeply transforms how you work. From solo projects to large team environments.

---

## 1. Core Concepts

### What is Version Control?
Version control tracks changes to files over time, letting you recall specific versions, understand what changed and why, and collaborate without overwriting others' work. Git is distributed. Every developer has a complete copy of the repository history.

### Key Git Concepts

| Concept | Description |
| :--- | :--- |
| **Repository (Repo)** | A project tracked by Git, containing all files and complete history. |
| **Commit** | A snapshot of your repository at a specific point in time. |
| **Branch** | A parallel version of your repository where you can work independently. |
| **HEAD** | A pointer to your current location (usually the latest commit on your branch). |
| **Remote** | A version of your repository hosted elsewhere (e.g., GitHub, GitLab). |
| **Working Directory** | The actual files you're editing on your machine. |
| **Staging Area (Index)** | A holding area for changes you want to include in the next commit. |
| **Merge** | Combining changes from different branches. |
| **Rebase** | Moving or replaying commits onto a different base commit. |

### The Three States of Git

1. **Modified**: You've changed a file but haven't staged it.
2. **Staged**: You've marked a modified file to go in the next commit.
3. **Committed**: The data is safely stored in your local repository.

---

## 2. Getting Started

### Initial Configuration

Set your identity once per machine:

```bash
# Set your name and email (used in every commit)
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Set default branch name to 'main'
git config --global init.defaultBranch main

# Set your default editor
git config --global core.editor "code --wait"  # VS Code
# or
git config --global core.editor "vim"

# View all configurations
git config --list

# View a specific config
git config user.name
```

### Creating a Repository

```bash
# Initialize a new repository in current directory
git init

# Initialize with a specific branch name
git init --initial-branch=main

# Clone an existing repository
git clone https://github.com/username/repo.git

# Clone to a specific directory
git clone https://github.com/username/repo.git my-folder

# Clone only recent history (faster for large repos)
git clone --depth 1 https://github.com/username/repo.git
```

### Ignoring Files

Create a `.gitignore` file to exclude files from version control:

```gitignore
# Dependencies
node_modules/
venv/
__pycache__/

# Environment files
.env
.env.local
*.key

# IDE files
.vscode/
.idea/
*.swp

# Build outputs
dist/
build/
*.pyc

# OS files
.DS_Store
Thumbs.db
```

---

## 3. Basic Workflow

### The Standard Cycle

```bash
# 1. Check status of your working directory
git status

# 2. Stage specific files
git add file1.py file2.js

# Stage all changes (use carefully)
git add .

# Stage only modified and deleted files (not new files)
git add -u

# Stage files interactively (review each change)
git add -p

# 3. Commit staged changes
git commit -m "Add user authentication feature"

# Stage and commit in one step (only for tracked files)
git commit -am "Fix bug in login validation"

# 4. Push to remote
git push origin main
```

### Viewing History

```bash
# View commit history
git log

# Compact one-line format
git log --oneline

# Show last 5 commits
git log -5

# Show commits with file changes
git log --stat

# Show commits with actual code changes
git log -p

# Graphical representation of branches
git log --graph --oneline --all --decorate

# Search commits by message
git log --grep="authentication"

# Search commits by author
git log --author="John"

# Show commits that modified a specific file
git log -- path/to/file.py

# Show who changed each line of a file
git blame file.py
```

### Viewing Changes

```bash
# Show unstaged changes
git diff

# Show staged changes
git diff --staged
# or
git diff --cached

# Show changes in a specific file
git diff file.py

# Compare branches
git diff main..feature-branch

# Compare commits
git diff abc123..def456
```

---

## 4. Branching Strategies

Branches are Git's killer feature. They let you work on features, experiments, or fixes independently without affecting the main codebase.

### Branch Basics

```bash
# List all local branches
git branch

# List all branches (local and remote)
git branch -a

# Create a new branch
git branch feature-login

# Create and switch to a new branch
git checkout -b feature-login
# or (modern syntax)
git switch -c feature-login

# Switch to an existing branch
git checkout main
# or
git switch main

# Delete a branch (safe - prevents deletion if unmerged)
git branch -d feature-login

# Force delete a branch
git branch -D feature-login

# Rename current branch
git branch -m new-name

# Rename a different branch
git branch -m old-name new-name
```

### Common Branching Models

#### 1. GitHub Flow (Simple and Modern)

Best for: Web apps, continuous deployment, small teams

```
main (always deployable)
  |
  |-- feature-user-auth (work happens here)
  |     |
  |     |-- commits
  |     |
  |   [Pull Request]
  |     |
  |<----| (merge back to main)
  |
  |-- feature-payment (another feature)
        |
        |-- commits
```

**Workflow:**
1. `main` is always stable and deployable
2. Create feature branches from `main`
3. Open Pull Request when ready
4. Merge to `main` after review
5. Deploy from `main`

```bash
# Start a new feature
git checkout main
git pull origin main
git checkout -b feature-dark-mode

# Work and commit
git add .
git commit -m "Add dark mode toggle"

# Push feature branch
git push -u origin feature-dark-mode

# Open Pull Request on GitHub
# After approval, merge via GitHub UI or:
git checkout main
git merge feature-dark-mode
git push origin main
git branch -d feature-dark-mode
```

#### 2. Git Flow (Complex but Structured)

Best for: Scheduled releases, large teams, enterprise

```
main (production)
  |
develop (integration branch)
  |
  |-- feature/user-auth
  |-- feature/payment
  |
  |-- release/1.2.0 (preparing for release)
  |     |
  |     |-- bugfixes
  |     |
  |---->| (merge to main and develop)
  |
  |-- hotfix/critical-bug (emergency fixes)
        |
        |---> main (immediate fix)
        |---> develop (keep in sync)
```

**Branch Types:**
- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: New features (branch from develop)
- `release/*`: Release preparation (branch from develop)
- `hotfix/*`: Emergency fixes (branch from main)

```bash
# Start a feature
git checkout develop
git checkout -b feature/user-auth

# Work and commit
git commit -am "Add authentication logic"

# Finish feature
git checkout develop
git merge --no-ff feature/user-auth
git branch -d feature/user-auth

# Start a release
git checkout -b release/1.2.0 develop
# Make release-specific commits
git checkout main
git merge --no-ff release/1.2.0
git tag -a v1.2.0 -m "Release version 1.2.0"
git checkout develop
git merge --no-ff release/1.2.0
git branch -d release/1.2.0

# Emergency hotfix
git checkout -b hotfix/critical-fix main
# Fix and commit
git checkout main
git merge --no-ff hotfix/critical-fix
git tag -a v1.2.1 -m "Hotfix 1.2.1"
git checkout develop
git merge --no-ff hotfix/critical-fix
git branch -d hotfix/critical-fix
```

#### 3. Trunk-Based Development (High Velocity)

Best for: Continuous deployment, mature CI/CD, experienced teams

```
main (trunk)
  |
  |<-- short-lived branches (< 1 day)
  |<-- direct commits
  |
  |-- feature flags control releases
```

**Key Principles:**
- All developers commit to `main` frequently (at least daily)
- Branches are short-lived (< 24 hours)
- Feature flags hide incomplete work
- Strong test automation required

```bash
# Create short-lived branch
git checkout -b add-button main

# Make small change
git commit -am "Add export button (behind feature flag)"

# Merge back quickly
git checkout main
git merge add-button
git push origin main
git branch -d add-button
```

---

## 5. Commit Best Practices

Good commits are the foundation of maintainable projects. They tell a story of what changed and why.

### Commit Message Conventions

**Conventional Commits Format:**

```
<type>([optional scope]): <description>

[optional body]

[optional footer(s)]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, semicolons)
- `refactor`: Code restructuring without changing behavior
- `perf`: Performance improvements
- `test`: Adding or modifying tests
- `build`: Build system or dependency changes
- `ci`: CI configuration changes
- `chore`: Other changes that don't modify src or test files

**Examples:**

```bash
# Good commit messages
git commit -m "feat: add user authentication with JWT"
git commit -m "fix: resolve null pointer exception in payment flow"
git commit -m "docs: update API documentation for /users endpoint"
git commit -m "refactor: extract validation logic into separate module"
git commit -m "perf: optimize database queries with indexing"

# With scope
git commit -m "feat(auth): add OAuth2 login support"
git commit -m "fix(api): handle timeout errors gracefully"

# With body
git commit -m "feat: add password reset functionality

Users can now request a password reset email. The token expires
after 1 hour for security. Updates user model and adds new endpoint.

Closes #123"

# Breaking changes
git commit -m "feat!: change API response format to match spec

BREAKING CHANGE: The /users endpoint now returns { data: [...] }
instead of a plain array. Update clients accordingly."
```

### Commit Guidelines

**DO:**
- Make atomic commits (one logical change per commit)
- Write clear, concise messages in present tense
- Explain WHY, not just WHAT (in commit body)
- Keep first line under 50 characters
- Keep subject and body separate with blank line
- Reference issue numbers when relevant

**DON'T:**
- Commit commented-out code or debug logs
- Use vague messages like "fix stuff" or "changes"
- Mix formatting changes with logic changes
- Commit secrets, credentials, or sensitive data
- Have commits like "fix previous commit" (use amend instead)

### Modifying Commits

```bash
# Add to the last commit (before pushing)
git add forgotten-file.py
git commit --amend --no-edit

# Change the last commit message
git commit --amend -m "New commit message"

# Undo last commit but keep changes
git reset --soft HEAD~1

# Undo last commit and discard changes (DANGEROUS)
git reset --hard HEAD~1

# Undo specific files from staging
git reset HEAD file.py

# Discard changes in working directory (DANGEROUS)
git checkout -- file.py
# or
git restore file.py
```

---

## 6. Merging and Rebasing

### Merging

Merging combines work from different branches. Git creates a merge commit that ties histories together.

```bash
# Merge feature into current branch
git merge feature-branch

# Merge with custom commit message
git merge feature-branch -m "Merge feature-branch into main"

# Merge without fast-forward (always create merge commit)
git merge --no-ff feature-branch

# Abort a merge
git merge --abort
```

**Fast-Forward vs. Non-Fast-Forward:**

```bash
# Fast-forward (linear history)
# main:    A -- B
# feature:         C -- D
# After merge: A -- B -- C -- D (no merge commit)

# Non-fast-forward (preserves branch history)
# main:    A -- B ----------- M
# feature:         C -- D --/
# After merge: Creates merge commit M
```

### Rebasing

Rebasing replays commits on top of another branch, creating a linear history.

```bash
# Rebase current branch onto main
git rebase main

# Interactive rebase (edit last 3 commits)
git rebase -i HEAD~3

# Continue after resolving conflicts
git rebase --continue

# Skip a commit during rebase
git rebase --skip

# Abort rebase
git rebase --abort
```

**When to Use Each:**

| Scenario | Use Merge | Use Rebase |
| :--- | :---: | :---: |
| Updating feature branch with latest main | | |
| Combining public branches | | |
| Cleaning up local commits before push | | |
| Preserving exact history | | |
| Linear, clean history | | |

**Golden Rule: Never rebase public branches** (branches others are working on)

### Interactive Rebase (History Editing)

```bash
# Rebase last 3 commits interactively
git rebase -i HEAD~3

# In the editor, you can:
# pick   = use commit
# reword = use commit, but edit message
# edit   = use commit, but stop for amending
# squash = combine with previous commit
# fixup  = like squash, but discard message
# drop   = remove commit
```

**Example interactive rebase:**

```
pick abc123 Add login feature
squash def456 Fix typo
reword ghi789 Update tests
drop jkl012 Debug logging

# Becomes:
# 1. Combined commit: "Add login feature" (with typo fix)
# 2. Reworded commit with new message
# 3. Debug commit removed
```

### Resolving Conflicts

```bash
# When conflicts occur, Git marks files:
<<<<<<< HEAD
Your current changes
=======
Incoming changes
>>>>>>> feature-branch

# To resolve:
# 1. Edit files to resolve conflicts
# 2. Remove conflict markers
# 3. Stage resolved files
git add resolved-file.py

# 4. Complete merge or rebase
git merge --continue
# or
git rebase --continue
```

**Conflict Resolution Tools:**

```bash
# Use visual merge tool
git mergetool

# Accept all changes from current branch
git checkout --ours file.py

# Accept all changes from incoming branch
git checkout --theirs file.py

# See conflicts
git diff --name-only --diff-filter=U
```

---

## 7. Working with Remotes

### Remote Basics

```bash
# List remotes
git remote -v

# Add a remote
git remote add origin https://github.com/user/repo.git

# Change remote URL
git remote set-url origin https://github.com/user/new-repo.git

# Remove a remote
git remote remove origin

# Rename a remote
git remote rename origin upstream

# Show remote details
git remote show origin
```

### Fetching, Pulling, and Pushing

```bash
# Fetch updates from remote (doesn't modify your work)
git fetch origin

# Fetch all remotes
git fetch --all

# Pull = fetch + merge
git pull origin main

# Pull with rebase instead of merge
git pull --rebase origin main

# Push to remote
git push origin main

# Push and set upstream (first time)
git push -u origin main
# Now you can just use: git push

# Push all branches
git push --all origin

# Push tags
git push --tags

# Force push (DANGEROUS - rewrites remote history)
git push --force origin main
# Safer alternative (fails if remote has new commits)
git push --force-with-lease origin main

# Delete remote branch
git push origin --delete feature-branch
```

### Upstream Tracking

```bash
# Set upstream for current branch
git branch --set-upstream-to=origin/main

# See which remote branch is tracked
git branch -vv

# Push and create remote branch with tracking
git push -u origin feature-new
```

---

## 8. Advanced Techniques and Hacks

### Stashing (Temporary Storage)

Save work without committing when you need to switch contexts.

```bash
# Stash current changes
git stash

# Stash with a message
git stash save "WIP: refactoring user model"

# List stashes
git stash list

# Apply most recent stash (keeps in stash list)
git stash apply

# Apply and remove from stash list
git stash pop

# Apply specific stash
git stash apply stash@{2}

# Show stash contents
git stash show -p stash@{0}

# Drop a specific stash
git stash drop stash@{0}

# Clear all stashes
git stash clear

# Create branch from stash
git stash branch new-branch-name
```

### Cherry-Picking

Apply specific commits from one branch to another.

```bash
# Apply a specific commit to current branch
git cherry-pick abc123

# Cherry-pick multiple commits
git cherry-pick abc123 def456 ghi789

# Cherry-pick without committing (stage only)
git cherry-pick -n abc123

# Abort cherry-pick
git cherry-pick --abort
```

### Tagging

Mark specific points in history (usually releases).

```bash
# Create lightweight tag
git tag v1.0.0

# Create annotated tag (recommended)
git tag -a v1.0.0 -m "Release version 1.0.0"

# Tag a specific commit
git tag -a v0.9.0 abc123 -m "Beta release"

# List tags
git tag

# Search tags
git tag -l "v1.*"

# Show tag details
git show v1.0.0

# Push tags to remote
git push origin v1.0.0
git push --tags

# Delete local tag
git tag -d v1.0.0

# Delete remote tag
git push origin --delete v1.0.0

# Checkout a tag (creates detached HEAD)
git checkout v1.0.0
```

### Reflog (Safety Net)

Reflog tracks all ref updates. Use it to recover "lost" commits.

```bash
# View reflog
git reflog

# View reflog for specific branch
git reflog show main

# Recover deleted branch/commit
git reflog
# Find the SHA of the lost commit
git checkout -b recovered-branch abc123

# Reset to a previous state
git reset --hard HEAD@{5}
```

### Bisect (Binary Search for Bugs)

Find the commit that introduced a bug.

```bash
# Start bisect
git bisect start

# Mark current commit as bad
git bisect bad

# Mark a known good commit
git bisect good abc123

# Git checks out a commit in the middle
# Test it, then mark it:
git bisect good  # if test passes
# or
git bisect bad   # if test fails

# Repeat until Git finds the problematic commit

# End bisect
git bisect reset

# Automated bisect with test script
git bisect start HEAD abc123
git bisect run ./test.sh
```

### Worktrees (Multiple Working Directories)

Work on multiple branches simultaneously without switching.

```bash
# Create a worktree
git worktree add ../project-feature feature-branch

# List worktrees
git worktree list

# Remove worktree
git worktree remove ../project-feature

# Prune deleted worktrees
git worktree prune
```

### Aliases (Time Savers)

```bash
# Create aliases
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status

# Useful complex aliases
git config --global alias.lg "log --graph --oneline --all --decorate"
git config --global alias.unstage "reset HEAD --"
git config --global alias.last "log -1 HEAD"
git config --global alias.visual "log --graph --oneline --all"
git config --global alias.amend "commit --amend --no-edit"

# Now you can use:
git lg
git unstage file.py
git amend
```

### Submodules (Dependencies)

Include other Git repositories as subdirectories.

```bash
# Add a submodule
git submodule add https://github.com/user/library.git libs/library

# Clone repo with submodules
git clone --recurse-submodules https://github.com/user/repo.git

# Initialize submodules in existing clone
git submodule init
git submodule update

# Update all submodules
git submodule update --remote

# Remove submodule
git submodule deinit libs/library
git rm libs/library
rm -rf .git/modules/libs/library
```

---

## 9. Collaboration Workflows

### Pull Request Workflow

1. **Fork and Clone** (open source) or **Clone** (team repo)
   ```bash
   git clone https://github.com/yourname/repo.git
   cd repo
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/add-search
   ```

3. **Make Changes and Commit**
   ```bash
   git add .
   git commit -m "feat: add search functionality"
   ```

4. **Keep Branch Updated**
   ```bash
   git fetch origin
   git rebase origin/main
   ```

5. **Push to Remote**
   ```bash
   git push -u origin feature/add-search
   ```

6. **Open Pull Request** on GitHub/GitLab

7. **Address Review Comments**
   ```bash
   git add .
   git commit -m "refactor: address review comments"
   git push
   ```

8. **Merge** (done by maintainer or via UI)

9. **Cleanup**
   ```bash
   git checkout main
   git pull origin main
   git branch -d feature/add-search
   ```

### Code Review Best Practices

**As Author:**
- Keep PRs small and focused (< 400 lines)
- Write clear PR descriptions
- Self-review before requesting review
- Respond to feedback promptly
- Don't force-push after review starts (unless necessary)

**As Reviewer:**
- Review within 24 hours when possible
- Be constructive and specific
- Approve when good enough, not perfect
- Test locally for complex changes
- Use suggestion comments for small fixes

---

## 10. Common Scenarios and Solutions

### Scenario: Accidentally Committed to Wrong Branch

```bash
# You're on main, but wanted to commit to feature branch
git log  # Copy the commit SHA (abc123)

git reset --soft HEAD~1  # Undo commit, keep changes
git stash  # Save changes

git checkout feature-branch
git stash pop  # Apply changes
git add .
git commit -m "Your message"
```

### Scenario: Need to Undo Last Push

```bash
# If no one else pulled yet
git reset --hard HEAD~1
git push --force-with-lease

# If others pulled (safer approach)
git revert HEAD
git push
```

### Scenario: Merge Wrong Branch

```bash
# Immediately after merge
git reset --hard HEAD~1

# If you already pushed
git revert -m 1 HEAD
git push
```

### Scenario: Lost Commits After Reset

```bash
git reflog
# Find the commit SHA before reset (abc123)
git reset --hard abc123
```

### Scenario: Remove File from History (Secrets)

```bash
# Remove from all history (REWRITES HISTORY)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/secrets.txt" \
  --prune-empty --tag-name-filter cat -- --all

# Push changes
git push --force --all

# Modern alternative (faster)
# Install git-filter-repo first
git filter-repo --path path/to/secrets.txt --invert-paths
```

### Scenario: Sync Fork with Upstream

```bash
# Add upstream remote
git remote add upstream https://github.com/original/repo.git

# Fetch upstream changes
git fetch upstream

# Merge upstream/main into your main
git checkout main
git merge upstream/main

# Or rebase your commits on top of upstream
git rebase upstream/main

# Push to your fork
git push origin main
```

---

## 11. Git Best Practices Summary

### Commit Practices
- Commit early and often
- Write meaningful commit messages
- Keep commits atomic and focused
- Use conventional commit format
- Don't commit broken code to main/develop
- Don't mix unrelated changes in one commit

### Branch Practices
- Use descriptive branch names (`feature/user-auth`, `fix/login-bug`)
- Delete merged branches
- Keep branches short-lived
- Regularly sync with main/develop
- Don't commit directly to main (use PRs)
- Don't rebase public branches

### Collaboration Practices
- Pull before push
- Use pull requests for code review
- Keep PRs small and focused
- Respond to review feedback
- Don't force push to shared branches
- Don't commit secrets or credentials

### History Practices
- Use `--force-with-lease` instead of `--force`
- Rebase local commits for clean history
- Use merge commits for feature integration
- Tag releases
- Don't rewrite public history
- Don't use `git add .` blindly

---

## 12. Troubleshooting

### Common Issues

**Problem: "Your branch and origin/main have diverged"**
```bash
# Option 1: Merge remote changes
git pull origin main

# Option 2: Rebase on remote (cleaner)
git pull --rebase origin main
```

**Problem: Detached HEAD state**
```bash
# Create a branch from current state
git checkout -b temp-branch

# Or return to a branch
git checkout main
```

**Problem: Merge conflicts**
```bash
# See conflicted files
git status

# Edit files, then:
git add <resolved-files>
git commit
```

**Problem: Forgot to create branch before committing**
```bash
git branch feature-new  # Create branch at current commit
git reset --hard origin/main  # Reset main to remote
git checkout feature-new  # Switch to feature branch
```

**Problem: Need to change author of commits**
```bash
# Change author of last commit
git commit --amend --author="New Name <newemail@example.com>"

# Change author of multiple commits
git rebase -i HEAD~3
# Mark commits as 'edit', then for each:
git commit --amend --author="New Name <newemail@example.com>"
git rebase --continue
```

---

## 13. Performance and Maintenance

### Keep Repository Healthy

```bash
# Clean up unnecessary files and optimize
git gc

# Aggressive cleanup
git gc --aggressive --prune=now

# Verify repository integrity
git fsck

# Remove untracked files and directories
git clean -fd

# Dry run (see what would be deleted)
git clean -fdn

# Prune remote-tracking branches
git remote prune origin
```

### Large Repositories

```bash
# Shallow clone (faster, less history)
git clone --depth 1 https://github.com/user/repo.git

# Fetch only specific branch
git clone -b main --single-branch https://github.com/user/repo.git

# Use Git LFS for large files
git lfs install
git lfs track "*.psd"
git add .gitattributes
```

---

## 14. Git Hooks

Automate tasks at key points in the Git workflow.

### Common Hooks

Located in `.git/hooks/`:
- `pre-commit`: Run before commit (linting, tests)
- `prepare-commit-msg`: Modify commit message template
- `commit-msg`: Validate commit message format
- `pre-push`: Run before push (tests, checks)

### Example: Pre-commit Hook (Python)

Create `.git/hooks/pre-commit`:

```bash
#!/bin/sh

# Run tests before commit
python -m pytest tests/

if [ $? -ne 0 ]; then
  echo "Tests failed. Commit aborted."
  exit 1
fi

# Run linter
python -m flake8 .

if [ $? -ne 0 ]; then
  echo "Linting failed. Commit aborted."
  exit 1
fi

exit 0
```

Make it executable:
```bash
chmod +x .git/hooks/pre-commit
```

### Tools for Hooks

- **Husky** (JavaScript): Manage Git hooks easily
- **pre-commit** (Python): Framework for managing hooks
- **lefthook** (Go): Fast parallel hook runner

---

## 15. Quick Reference

### Essential Commands

```bash
# Status and Info
git status                 # Check working directory
git log --oneline         # View commit history
git diff                  # See changes

# Branching
git branch                # List branches
git checkout -b feat      # Create and switch to branch
git merge feat            # Merge branch

# Committing
git add .                 # Stage all changes
git commit -m "message"   # Commit with message
git commit --amend        # Modify last commit

# Remote Operations
git pull                  # Fetch and merge
git push                  # Upload commits
git fetch                 # Download remote changes

# Undo Changes
git reset --soft HEAD~1   # Undo commit, keep changes
git reset --hard HEAD~1   # Undo commit, discard changes
git checkout -- file      # Discard file changes
git revert abc123         # Create commit that undoes abc123

# Advanced
git stash                 # Temporarily save changes
git rebase main           # Rebase on main
git cherry-pick abc123    # Apply specific commit
git reflog                # View all ref changes
```

---

## See Also

- **[CI/CD Pipeline Guide](CI_CD_Pipeline_Guide.md)** - Automating Git workflows with GitHub Actions
- **[Testing and Debugging Cheat Sheet](../cheatsheets/Testing_and_Debugging_Cheat_Sheet.md)** - Pre-commit testing strategies
- **[GLOSSARY.md](../GLOSSARY.md)** - Git and version control terminology

---

**Pro Tips:**

1. **Use `.gitignore` early** - Set it up before first commit
2. **Commit messages matter** - Future you will thank present you
3. **Branch liberally** - Branches are cheap, use them
4. **Pull before push** - Avoid conflicts
5. **Never commit secrets** - Use environment variables
6. **Learn interactive rebase** - Clean up history before sharing
7. **Use `--force-with-lease`** - Safer than `--force`
8. **Master `git reflog`** - It's your safety net
9. **Automate with hooks** - Catch issues before they're committed
10. **When in doubt, branch** - You can always delete it later

---

[Back to Main](../README.md)