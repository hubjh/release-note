from release_note.group.github_release import GithubRelease

class SeabornRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="seaborn", owner='mwaskom', repo='seaborn')