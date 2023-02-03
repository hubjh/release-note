from release_note.group.github_release import GithubRelease

class MatplotlibRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="matplotlib", owner='matplotlib', repo='matplotlib')