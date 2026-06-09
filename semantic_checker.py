def check_semantic_tags(tags):

    semantic_tags = [
        "header",
        "nav",
        "main",
        "section",
        "article",
        "footer"
    ]

    found = []
    missing = []

    for tag in semantic_tags:

        if tag in tags:
            found.append(tag)
        else:
            missing.append(tag)

    return found, missing