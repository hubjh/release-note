from release_note.group.github_release import GithubRelease

class EmotionRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="emotion", owner='emotion-js', repo='emotion')