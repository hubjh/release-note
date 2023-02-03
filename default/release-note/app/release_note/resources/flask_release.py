from release_note.group.github_release import GithubRelease

class FlaskRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="flask", owner='pallets', repo='flask')