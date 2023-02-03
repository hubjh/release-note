from release_note.group.github_release import GithubRelease

class GraphqlRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="graphql-js", owner='graphql', repo='graphql')