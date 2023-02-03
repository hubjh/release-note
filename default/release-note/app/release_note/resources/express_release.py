from release_note.group.github_release import GithubRelease

class ExpressRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="express", owner='expressjs', repo='express')