import git
from . import repo


class GitCore(git.Git):
    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base = master

        self.repo = None

    def open_repo(self):
        try:
            self.repo = repo.GitRepo(self.base.active_dir)
        except git.exc.InvalidGitRepositoryError:
            self.repo = None

    def get_version(self):
        return self.version()

    def get_active_branch(self):
        if self.repo is None:
            return "Not a repo"
        return self.repo.active_branch.name
