class Quote:
    """A quote object."""

    def __init__(self, body: str, author: str):
        """Create a new 'Quote'.

        :param body: Body of the quote.
        :param author: Author of the quote.
        """
        self.body = body.strip('"')
        self.author = author

    def __eq__(self, other):
        """Compare self with another 'Quote' object."""
        return self.body == other.body and self.author == other.author

    def __repr__(self):
        """Return `repr(self)`."""
        return f'Quote(body={self.body}, author={self.author})'

    def __str__(self):
        """Return `str(self)`."""
        return f'"{self.body}" - {self.author}'
