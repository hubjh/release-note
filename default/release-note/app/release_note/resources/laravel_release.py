from release_note.group.github_release import GithubRelease

class LaravelRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="laravel", owner='laravel', repo='laravel')