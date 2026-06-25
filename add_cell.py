import json
import sys
import os

def add_cell(notebook_path, cell_type, source):
    if os.path.exists(notebook_path):
        with open(notebook_path, 'r') as f:
            nb = json.load(f)
    else:
        nb = {
            "cells": [],
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3"
                },
                "language_info": {
                    "codemirror_mode": {"name": "ipython", "version": 3},
                    "file_extension": ".py",
                    "mimetype": "text/x-python",
                    "name": "python",
                    "nbconvert_exporter": "python",
                    "pygments_lexer": "ipython3",
                    "version": "3.9.0"
                }
            },
            "nbformat": 4,
            "nbformat_minor": 5
        }
    
    cell = {
        "cell_type": cell_type,
        "metadata": {},
        "source": [line + '\n' for line in source.split('\n')]
    }
    # Clean up the last newline
    if cell["source"] and cell["source"][-1].endswith('\n'):
        cell["source"][-1] = cell["source"][-1][:-1]
        
    if cell_type == "code":
        cell["execution_count"] = None
        cell["outputs"] = []
        
    nb["cells"].append(cell)
    
    with open(notebook_path, 'w') as f:
        json.dump(nb, f, indent=1)

if __name__ == "__main__":
    notebook_path = sys.argv[1]
    cell_type = sys.argv[2]
    source_file = sys.argv[3]
    with open(source_file, 'r') as f:
        source = f.read()
    # remove trailing newline from source if it exists because file read adds it
    if source.endswith('\n'):
        source = source[:-1]
    add_cell(notebook_path, cell_type, source)
