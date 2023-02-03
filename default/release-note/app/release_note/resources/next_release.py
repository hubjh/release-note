from release_note.group.github_release import GithubRelease

class NextRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="next", owner='vercel', repo='next.js')