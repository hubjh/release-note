from release_note.group.github_release import GithubRelease

class TailwindRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="tailwind", owner='tailwindlabs', repo='tailwindcss')