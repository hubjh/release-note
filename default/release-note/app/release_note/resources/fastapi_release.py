from release_note.group.github_release import GithubRelease

class FastapiRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="fastapi", owner='tiangolo', repo='fastapi')