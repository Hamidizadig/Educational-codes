class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self) -> str:
        pass

    def __eq__(sel, o: object) -> bool:
        pass

    def __hash__(self) -> int:
        pass

    @property
    def name(self):
        return self.a
