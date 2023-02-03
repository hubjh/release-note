from release_note.group.github_release import GithubRelease

class RailsRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="rails", owner='rails', repo='rails')