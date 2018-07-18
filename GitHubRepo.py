from datetime import datetime
import logging
import time

import github
from github.GithubObject import NotSet

class GitHubRepo(object):

    LABELS = {}
    MILESTONES = {}

    def __init__(self, **kwargs):

        self.token = kwargs.pop("token")
        self.repo_name = kwargs.pop("repository")

        self.conn = None
        self.repo = None

    def connect(self):

        try:
            logging.info("Trying to connect to the GitHub API server!")
            self.conn = github.Github(self.token)

            # Get correct repo
            self.repo = self.conn.get_repo(self.repo_name)

            logging.info("Successfully connected to GitHub!")
        except:
            logging.error("Could not connect to the GitHub server!")
            raise

    def add_label(self, name=None, color=None, description=None):

        # Check if the required fields are provided
        if not name or not color:
            logging.error("Cannot add label as no name or color was provided!")
            raise RuntimeError("Label could not be added!")

        # Substituting None's with the correct value
        description = NotSet if description is None else description

        # Add label to repo
        self.LABELS[name] = self.repo.create_label(name=name,
                                                   color=color.strip("#"),
                                                   description=description)

    def add_milestone(self, title=None, state=None, description=None, due_on=None):

        # Check if the required fields are provided
        if not title:
            logging.error("Cannot add milestone as no title was provided!")
            raise RuntimeError("Milestone could not be added!")

        # Substituting None's with the correct value
        state = NotSet if state is None else state
        description = NotSet if description is None else description
        due_on = NotSet if due_on is None else datetime.strptime(due_on, "%Y-%m-%d")

        # Add milestone to repo
        self.MILESTONES[title] = self.repo.create_milestone(title=title,
                                                            state=state,
                                                            description=description,
                                                            due_on=due_on)

    def add_issue(self, title=None, body=None, assignees=None, milestone=None, labels=None, state=None):

        # Check if the required fields are provided
        if not title:
            logging.error("Cannot add issue as no title was provided!")
            raise RuntimeError("Issue could not be added!")

        # Substituting None's with the correct value
        body = NotSet if body is None else body
        assignees = NotSet if assignees is None else assignees
        milestone = NotSet if milestone is None else self.MILESTONES[milestone]
        labels = NotSet if labels is None else map(lambda l_name: self.LABELS[l_name], labels)
        state = NotSet if state is None else state

        # Add issue to repo
        issue = self.repo.create_issue(title=title,
                                       body=body,
                                       assignees=assignees,
                                       milestone=milestone,
                                       labels=labels)

        # Update state
        issue.edit(state=state)

