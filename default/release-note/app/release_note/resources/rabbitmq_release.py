from release_note.group.github_release import GithubRelease

class RabbitmqRelease(GithubRelease):
    def __init__(self):
        super().__init__(product_name="rabbitmq", owner='rabbitmq', repo='rabbitmq-server')