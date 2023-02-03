from release_note.group.github_release import GithubRelease

class NestRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="nest", owner='nestjs', repo='nest')