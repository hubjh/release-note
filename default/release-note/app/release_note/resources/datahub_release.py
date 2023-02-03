from release_note.group.github_release import GithubRelease

class DatahubRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="datahub", owner='datahub-project', repo='datahub')