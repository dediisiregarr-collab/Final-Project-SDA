def collect_tags(node, tags):

    if node is None:
        return

    tags.append(node.tag)

    for child in node.children:
        collect_tags(child, tags)


def unique_tags(root):

    tags = []

    collect_tags(root, tags)

    return sorted(set(tags))


def most_used_tag(root):

    tags = []

    collect_tags(root, tags)

    counter = {}

    for tag in tags:
        counter[tag] = counter.get(tag, 0) + 1

    max_count = max(counter.values())

    most_used = []

    for tag, count in counter.items():
        if count == max_count:
            most_used.append(tag)

    return most_used, max_count