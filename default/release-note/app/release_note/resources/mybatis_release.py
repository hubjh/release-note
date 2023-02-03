from release_note.group.github_release import GithubRelease

class MybatisRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="mybatis", owner='mybatis', repo='mybatis-3')