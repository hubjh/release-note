from release_note.group.github_release import GithubRelease

class VuexRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="vuex", owner='vuejs', repo='vuex')