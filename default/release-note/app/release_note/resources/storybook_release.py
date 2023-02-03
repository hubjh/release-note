from release_note.group.github_release import GithubRelease

class StorybookRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="storybook", owner='storybookjs', repo='storybook')