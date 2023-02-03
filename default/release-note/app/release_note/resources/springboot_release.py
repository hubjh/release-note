from release_note.group.github_release import GithubRelease

class SpringbootRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="springboot", owner='spring-projects', repo='spring-boot')