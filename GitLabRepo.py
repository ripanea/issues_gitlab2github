import logging

import gitlab

class GitLabRepo(object):

    def __init__(self, **kwargs):

        self.URL = kwargs.pop("URL")
        self.token = kwargs.pop("token")
        self.repo_name = kwargs.pop("repository")

        self.conn = None
        self.project = None

    def connect(self):

        try:
            logging.info("Trying to connect to the GitLab API server!")
            self.conn = gitlab.Gitlab(self.URL, private_token=self.token)
            self.conn.auth()

            # Select correct project
            self.project = self.conn.projects.get(self.repo_name)

            logging.info("Successfully connected to GitLab!")
        except:
            logging.error("Could not connect to the GitLab server!")
            raise

    def iter_labels(self):
        return self.project.labels.list(as_list=False, sort="asc")

    def iter_milestones(self):
        return self.project.milestones.list(as_list=False, sort="asc")

    def iter_issues(self):
        # Yield all issues from the project
        return self.project.issues.list(as_list=False, sort="asc")
