from release_note.group.github_release import GithubRelease

class KubernetesRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="kubernetes", owner='kubernetes', repo='kubernetes')
