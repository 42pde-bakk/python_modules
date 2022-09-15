class CsvReader:
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = max(0, skip_top)  # Can't be lower than 0
        self.skip_bottom = max(0, skip_bottom)
        self.lines = list()
        self.data = list()
        self.f = None
        print(f'done with init')

    def __enter__(self):
        print(f'in enter')
        try:
            self.f = open(self.filename, 'r')
        except FileNotFoundError:
            return None
        lines = self.f.read().splitlines()
        if len(lines) == 0:
            return None
        self.lines = [list(map(str.strip, line.split(self.sep))) for line in lines]
        self.skip_top = min(len(self.lines), self.skip_top)  # Can't be bigger than len(lines)
        self.skip_bottom = min(len(self.lines), self.skip_bottom)
        self.data = self.lines[self.skip_top: len(self.lines) - self.skip_bottom]
        column_amount = len(self.lines[0])
        if any([len(line) != column_amount for line in self.lines]):
            return None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.f is not None:
            self.f.close()

    def getdata(self):
        return self.data

    def getheader(self):
        if self.header:
            return self.lines[0]
        return None
