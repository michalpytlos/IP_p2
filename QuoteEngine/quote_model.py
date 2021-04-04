class Quote:

    def __init__(self, body: str, author: str):
        self.body = body.strip('"')
        self.author = author

    def __eq__(self, other):
        return self.body == other.body and self.author == other.author

    def __repr__(self):
        return f'Quote(body={self.body}, author={self.author})'

    def __str__(self):
        return f'"{self.body}" - {self.author}'
