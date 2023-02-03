from release_note.group.github_release import GithubRelease

class MobxRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="mobx", owner='mobxjs', repo='mobx')