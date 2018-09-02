"""Helper methods for groups"""


def convertGroup(group):
    if(isinstance(group, str)):
        return [group]
    if group is None:
        return []
    assert isinstance(group, list), f"{group} must be a list or string"
    return group
