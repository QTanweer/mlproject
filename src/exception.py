import sys # gives info about runtime environment i.e. it will have info about any exceptions in runtime automatically
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error in file: " + str(file_name) + " at line: " + str(exc_tb.tb_lineno) + " with error: " + str(error)
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail= error_detail)
    
    def __str__(self) -> str:
        return self.error_message
    
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.error("An error occurred")
        logging.exception(e)
        raise CustomException("An error occurred", e) from e


# if __name__ == "__main__":   # trying custom exception
#     try:
#         a = 1/0
#     except Exception as e:
#         # logging.error("Zero Division Error")
#         # logging.error(error_message_detail(e, sys))
#         # logging.error(CustomException(e, sys))
#         # logging.error(CustomException(e, sys).__str__())
#         # logging.error(CustomException(e, sys).error_message)

        

#         logging.info("Zero Division Error")
#         raise CustomException(e, sys) from e
    

