from release_note.group.github_release import GithubRelease

class AngularRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="angular", owner='angular', repo='angular')