from release_note.group.github_release import GithubRelease

class CeleryRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="celery", owner='celery', repo='celery')