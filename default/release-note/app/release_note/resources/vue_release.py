from release_note.group.github_release import GithubRelease

class VueRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="vue", owner='vuejs', repo='vue')