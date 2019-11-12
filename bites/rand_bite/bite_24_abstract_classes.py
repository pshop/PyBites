from abc import ABC, abstractmethod


class Challenge(ABC):

    def __init__(self, number, title):
        self.number = number
        self.title = title
        super(Challenge, self).__init__()

    @abstractmethod
    def verify(self, something):
        pass

    @property
    @abstractmethod
    def pretty_title(self):
        pass


class BlogChallenge(Challenge):

    def __init__(self, number, title, merged_prs):
        super().__init__(number, title)
        self.merged_prs = merged_prs

    def verify(self, something):
        if something in self.merged_prs:
            return True
        return False

    @property
    def pretty_title(self):
        return 'PCC1 - Wordvalues'


class BiteChallenge(Challenge):

    def __init__(self, number, title, result):
        super().__init__(number, title)
        self.merged_prs = result

    def verify(self, something):
        if something in self.merged_prs:
            return True
        return False

    @property
    def pretty_title(self):
        return 'Bite 24. ABC and class inheritance'


if __name__ == '__main__':
    merged_prs_lol = [41, 42, 44]
    blog = BlogChallenge(1, 'hello', merged_prs_lol)
    print(blog.verify(41))