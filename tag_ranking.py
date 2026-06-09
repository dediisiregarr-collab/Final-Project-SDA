def collect_tags(node, tags):

    if node is None:
        return

    tags.append(node.tag)

    for child in node.children:
        collect_tags(child, tags)


def get_tag_ranking(root):

    tags = []

    collect_tags(root, tags)

    counter = {}

    for tag in tags:
        counter[tag] = counter.get(tag, 0) + 1

    ranking = sorted(
        counter.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return ranking