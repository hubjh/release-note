from release_note.group.github_release import GithubRelease

class ReduxRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="redux", owner='reduxjs', repo='redux')
