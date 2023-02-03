from release_note.group.github_release import GithubRelease

class PrometheusRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="prometheus", owner='prometheus', repo='prometheus')