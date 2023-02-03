from release_note.group.github_release import GithubRelease

class NuxtRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="nuxt", owner='nuxt', repo='framework')