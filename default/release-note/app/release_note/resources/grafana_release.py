from release_note.group.github_release import GithubRelease

class GrafanaRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="grafana", owner='grafana', repo='grafana')