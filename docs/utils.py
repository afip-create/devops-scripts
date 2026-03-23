# utils.py

import logging
import os
import re
import shutil
import subprocess
import sys

from typing import List, Optional, Tuple

def get_env_variable(var_name: str) -> str:
    """Get the environment variable or raise an error."""
    if var_name not in os.environ:
        raise ValueError(f"Environment variable {var_name} is not set")
    return os.environ[var_name]

def get_cluster_nodes() -> List[str]:
    """Get the list of cluster nodes from the environment variable."""
    return get_env_variable("CLUSTER_NODES").split(",")

def get_cluster_nodes_pattern() -> str:
    """Get the pattern for the cluster nodes from the environment variable."""
    return get_env_variable("CLUSTER_NODES_PATTERN")

def get_cluster_config() -> str:
    """Get the cluster configuration from the environment variable."""
    return get_env_variable("CLUSTER_CONFIG")

def get_devops_project() -> str:
    """Get the DevOps project name from the environment variable."""
    return get_env_variable("DEVOPS_PROJECT")

def execute_command(command: str) -> Tuple[str, str]:
    """Execute a command and return the output and error."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode("utf-8"), error.decode("utf-8")

def execute_script(script_path: str) -> Tuple[str, str]:
    """Execute a script and return the output and error."""
    output, error = execute_command(f"bash {script_path}")
    return output, error

def copy_file(source_path: str, destination_path: str) -> None:
    """Copy a file from one location to another."""
    shutil.copy(source_path, destination_path)

def get_revision() -> str:
    """Get the Git revision from the environment variable."""
    return get_env_variable("GITHUB_REPOSITORY")

def get_commit_hash() -> str:
    """Get the Git commit hash from the environment variable."""
    return get_env_variable("GITHUB_SHA")