import io


class FileParser:
    """
		Base Class for File Parsing.
		Inherit from this File to implement custom file parsing
	"""

    def __init__(self, file):
        """
			Arguments:
				- file: the file to be parsed
		"""

        acceptable_arg_type_conditions = [
            isinstance(file, io.TextIOBase),
            isinstance(file, io.BufferedIOBase),
            isinstance(file, io.RawIOBase),
            isinstance(file, io.IOBase),
            isinstance(file, str),
        ]

        if not any(acceptable_arg_type_conditions):
            raise ValueError(
                f"{self.__class__.__name__} expects a File-Type Object or str"
            )

        if isinstance(file, str):
            try:
                self.file = open(file, "r")
            except Exception as e:
                raise e
        else:
            self.file = file
