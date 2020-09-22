STRING_INDICATORS = ["'", '"']

class Token(str):
    def __init__(self, *args, **kwargs)
        super(Token, self).__init__(*args, **kwargs)

    @staticmethod
    def _is_int(text):
        return text.isnumeric()

    @staticmethod
    def _is_float(text):
        if '.' in text:
            if text.replace('.', '', 1).isdecimal():
                return True
        return False

    @staticmethod
    def _is_string(text):
        for char in STRING_INDICATORS:
            if text.startswith(char) and text.endswith(char):
                return True
        return False

    @staticmethod
    def _is_list(text):
        pass

    @staticmethod
    def _is_dict(text):
        pass