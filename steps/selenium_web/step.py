from functools import cached_property

class Step:
    """
    被case调用
    """
    def __init__(self):
        """
        初始化方法
        """
        pass
    
    @cached_property
    def selenium_web_form(self):
        from . import selenium_web_form
        
        _step = selenium_web_form.Step()

        return _step