"""

Displays messages to console.

"""

from modules.screenclr import clearscreen


def ascii_art(version: str) -> None:
    """Displays ASCII Art and Version to console."""
    clearscreen()
    print(
        f"""
    V{version}                
    ██████╗  █████╗ ██████╗ ███████╗██████╗  ██████╗██╗   ██╗████████╗                    
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝██║   ██║╚══██╔══╝                    
    ██████╔╝███████║██████╔╝█████╗  ██████╔╝██║     ██║   ██║   ██║                       
    ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗██║     ██║   ██║   ██║                       
    ██║     ██║  ██║██║     ███████╗██║  ██║╚██████╗╚██████╔╝   ██║                       
    ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝    ╚═╝                       
    ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗                            
    ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝                            
    ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   ███████╗                            
    ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║                            
    ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████║                            
    ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝                            
    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
    ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
    ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
    ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                  :8r@nd0n       
    """
    )


def token_error():
    """Message to display if token has expired."""
    print(
        """
  It looks like your token is expired. 
  Deleting 'token.pickle' and attempting to reauthorize.
          """
    )


def readme():
    """Read me message."""
    clearscreen()
    print(
        """
        
                ██████╗ ███████╗ █████╗ ██████╗     ███╗   ███╗███████╗
                ██╔══██╗██╔════╝██╔══██╗██╔══██╗    ████╗ ████║██╔════╝
                ██████╔╝█████╗  ███████║██║  ██║    ██╔████╔██║█████╗  
                ██╔══██╗██╔══╝  ██╔══██║██║  ██║    ██║╚██╔╝██║██╔══╝  
                ██║  ██║███████╗██║  ██║██████╔╝    ██║ ╚═╝ ██║███████╗
                ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝╚══════╝
                                                           
"""
    )
