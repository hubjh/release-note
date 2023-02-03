from packaging.version import parse as parse_version

def is_version_matched(version, min_version, max_version):
    if min_version and parse_version(version) < parse_version(min_version):
        return False
    
    if max_version and parse_version(version) > parse_version(max_version):
        return False

    return True

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)