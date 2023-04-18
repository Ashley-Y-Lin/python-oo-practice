class SerialGenerator:
    """Machine to create unique incrementing serial numbers."""

    def __init__(self, start):
        """
        Creates a new serial number
        >>> serial = SerialGenerator(start=100)
        """
        self.start = start
        self.count = start

    def __repr__(self):
        return f"<start value={self.start}, current value={self.count}>"

    def generate(self):
        """
        Returns the next sequential number
        >>> serial = SerialGenerator(start=100)

        >>> serial.generate()
        100

        >>> serial.generate()
        101

        >>> serial.generate()
        102
        """
        # could also just subtract 1 from return value
        output = self.count
        self.count += 1
        return output

    def reset(self):
        """
        Resets the serial number to original start number
        >>> serial = SerialGenerator(start=100)

        >>> serial.generate()
        100

        >>> serial.generate()
        101

        >>> serial.generate()
        102

        >>> serial.reset()

        >>> serial.generate()
        100
        """
        self.count = self.start
