from release_note.group.github_release import GithubRelease

class ElasticsearchRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="elasticsearch", owner='elastic', repo='elasticsearch')