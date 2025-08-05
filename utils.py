import requests

def get_default_branch(token, owner, repo):
    """
    Retrieve the default branch name of the specified GitHub repository.

    Args:
        token (str): GitHub access token.
        owner (str): Repository owner (user or org).
        repo (str): Repository name.

    Returns:
        str: The name of the default branch.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json().get("default_branch", "main")

def check_workflow_presence(token, owner, repo, workflow_files):
    """
    Check if all specified workflow files exist in the given repository.

    Args:
        token (str): GitHub access token.
        owner (str): Repository owner (user or org).
        repo (str): Repository name.
        workflow_files (list): List of workflow file names to check.

    Returns:
        bool: True if all workflow files are present, False otherwise.
    """
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }
    for wf in workflow_files:
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/.github/workflows/{wf}"
        r = requests.get(url, headers=headers)
        if r.status_code == 404:
            return False
    return True
