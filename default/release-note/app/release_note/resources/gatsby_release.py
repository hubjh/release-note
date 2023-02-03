from release_note.group.github_release import GithubRelease

class GatsbyRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="gatsby", owner='gatsbyjs', repo='gatsby')