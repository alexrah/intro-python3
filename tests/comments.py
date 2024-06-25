tReturnComment = tuple[str, str]


def comment_block() -> tReturnComment:
    """Intro

    prova di testo per docstring

    """
    return '2', '4'


if __name__ == '__main__':
    print(comment_block())
