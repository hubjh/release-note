from release_note.group.github_release import GithubRelease

class LiquibaseRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="liquibase", owner='liquibase', repo='liquibase')