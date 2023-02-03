from release_note.group.github_release import GithubRelease

class PandasRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="pandas", owner='pandas-dev', repo='pandas')