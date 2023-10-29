import logging

# logging.basicConfig(level="INFO")


class longest_substring:
    def __init__(self) -> None:
        logging.info("class longest_substring created")
        self.s = ""
        self.len_longest_substring = 0

    def set(self, s):
        self.s = s

    def get_s(self):
        logging.info(self.s)

    def find_substring(self):
        l = []
        longest_substring = []
        for a in self.s:
            logging.info(f"l:{l}")
            if a in l:
                longest_substring = l.copy()
                logging.info(f"longest_substring: {longest_substring}")
                logging.info(f"{a} in {l}")
                if len(l) > len(longest_substring):
                    longest_substring.clear()
                    longest_substring.append(l)
                elif len(l) < len(longest_substring):
                    pass
                l.clear()
                l.append(a)
            else:
                logging.info(f"{a} not in {l}")
                l.append(a)
        if len(l) > len(longest_substring):
            longest_substring.clear()
            longest_substring = l.copy()
        logging.info(f"longest_substring: {longest_substring}")
        self.len_longest_substring = len(longest_substring)
        return


def main():
    s = "abcabcd"
    foo = longest_substring()
    foo.set(s)
    foo.get_s()
    foo.find_substring()


if __name__ == "__main__":
    main()
