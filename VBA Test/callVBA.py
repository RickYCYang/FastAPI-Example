import os
import win32com.client

# Open Excel Application
excel = win32com.client.Dispatch("Excel.Application")

# Prepare target VBA path
vba_filename = "VBA.xlsm"
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, vba_filename)

# Open VBA
# Absolute path is also ok => (Filename="E:\VBA.xlsm")
excel.Workbooks.Open(Filename = filename) 

# Case 1: Run the macro without parameter
excel.Application.Run("VBA.xlsm!hello")

# Case 2: Run the macro with parameter and get the return from VBA
result = excel.Application.Run("VBA.xlsm!hello2", "Rick Test")
print(result)

# Quit the excel application
excel.Application.Quit()

# Delete excel process
del excel