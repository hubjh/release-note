from release_note.group.github_release import GithubRelease

class ReactRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="react", owner='facebook', repo='react')
