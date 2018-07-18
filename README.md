# Migrate issues from Gitlab to Github

This tool migrates the *issues*, *labels*, and *milestones* from a **GitLab** repository to a **GitHub** repository. 

## Requirements

You will need to install a set of Python packages. To do that, run the following command in your terminal:

```bash
sudo pip install -U python-gitlab pygithub
```

## How to run?

1. Make a copy of `template_config.json` and fill in with your repositories information. 

2. Run the tool as following:

    ```bash
    ./migrate_issues --config=config.json -vv
    ```
    
    ... where `config.json` is your new configuration file. 

---
***Note:*** You can specify the verbosity level by using the `-v` tag multiple time. There are maximum 3 levels or verbosity.

---

## Usage

    usage: migrate_issues [-h] -c CONFIG_FILE [-v]
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG_FILE, --config CONFIG_FILE
                            Path to config file.
      -v                    Increase verbosity of the program.Multiple -v's increase the verbosity level:
                               0 = Errors
                               1 = Errors + Warnings
                               2 = Errors + Warnings + Info
                               3 = Errors + Warnings + Info + Debug
