from release_note.group.github_release import GithubRelease

class NodeRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="node", owner='nodejs', repo='node')