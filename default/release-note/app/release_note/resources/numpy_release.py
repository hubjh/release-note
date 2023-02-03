from release_note.group.github_release import GithubRelease

class NumpyRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="numpy", owner='numpy', repo='numpy')