from release_note.group.github_release import GithubRelease

class DeltaLakeRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="delta_lake", owner='delta-io', repo='delta')