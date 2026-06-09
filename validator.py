from stack import Stack

def validate(tokens):

    stack = Stack()

    history = []
    step=1

    for token in tokens:

        # Tag pembuka
        if token.startswith("<") and not token.startswith("</"):

            tag = token[1:-1]

            stack.push(tag)

            history.append(
                f"""
            STEP {step}

            Push <{tag}>

            Stack:
            {chr(10).join(f'[{x}]' for x in reversed(stack.get_items()))}

            --------------------------
            """
            )

            step += 1

        # Tag penutup
        elif token.startswith("</"):

            tag = token[2:-1]

            if stack.is_empty():

                history.append(f"ERROR: </{tag}> tidak punya pasangan")

                return (
                    False,
                    f"Tag </{tag}> tidak memiliki pasangan pembuka",
                    history
                )

            top = stack.pop()

            history.append(
                f"""
            STEP {step}

            Pop <{top}>

            Stack:
            {chr(10).join(f'[{x}]' for x in reversed(stack.get_items()))}

            --------------------------
            """
            )

            step += 1

            if top != tag:

                history.append(
                    f"ERROR: <{top}> ditutup oleh </{tag}>"
                )

                return (
                    False,
                    f"Tag <{top}> ditutup dengan </{tag}>",
                    history
                )   

    if not stack.is_empty():

        remaining = stack.pop()

        history.append(
            f"ERROR: <{remaining}> belum ditutup"
        )

        return (
            False,
            f"Error: Tag <{remaining}> belum ditutup",
            history
        )

    history.append("HTML VALID")

    return True, "HTML Valid", history