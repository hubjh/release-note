from release_note.group.github_release import GithubRelease

class FlinkRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="flink", owner='apache', repo='flink')
