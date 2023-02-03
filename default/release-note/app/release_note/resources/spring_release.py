from release_note.group.github_release import GithubRelease

class SpringRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="spring", owner='spring-projects', repo='spring-framework')