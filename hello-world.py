    from typing import IO
    from io import IOBase
    from sys import stdout
    
    
    class MessageFormatter():
        __terminator: str
        def __init__(self, terminator: str):
            """Create a new MessageFormatter"""
            if not isinstance(terminator, str):
                raise TypeError(f"terminator must be a str")
                
            self.__terminator = terminator
        
    
        def set_terminator(self, terminator: str):
            """Set termination character(s)"""
            if not isinstance(terminator, str):
                raise TypeError(f"terminator must be a str")
            
            self.__terminator = terminator
    
        def get_terminator(self) -> str:
            """Get termination character(s)"""
            return self.__terminator
    
    
        def format(self, message: str) -> str:
            """Formats a given message"""
            if not isinstance(message, str):
                raise TypeError(f"message must be a str")
            return f"{message}{self.__terminator}"
    
    
    class Printer:
        __target: IO
        __message: str
    
        def __init__(self, target: IO, message: str):
            """Creates a new Printer"""
            if not isinstance(target, IOBase):
                raise TypeError(f"target must be a file object")
            if not isinstance(message, str):
                raise TypeError(f"message must be a str")
            
            self.__target = target
            self.__message = message
    
    
        def set_target(self, target: IO):
            """Sets the printer target (destination file object)"""
            if not isinstance(target, IOBase):
                raise TypeError(f"target must be a file object")
    
            self.__target = target
        
        def get_target(self) -> IO:
            """Gets the printer target (destination file object)"""
            return self.__target
        
    
        def set_message(self, message: str):
            """Sets the printer message"""
            if not isinstance(message, str):
                raise TypeError(f"message must be a str")
    
            self.__message = message
        
        def get_message(self) -> str:
            """Gets the printer message"""
            return self.__message
            
    
        def print_message(self, formatter: MessageFormatter):
            """Formats the message with the given formatter, and prints to target"""
            output = formatter.format(self.__message)
            self.__target.write(output)
    
    
    if __name__ == "__main__":
        formatter = MessageFormatter("\n")
    
        printer = Printer(stdout, "Hello world")
        printer.print_message(formatter)