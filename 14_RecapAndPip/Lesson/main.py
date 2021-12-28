import subprocess
import sys

try:
    from prettytable import PrettyTable
except:
    print("prettytable not installed. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'prettytable'])
    from prettytable import PrettyTable


table = PrettyTable(["animal", "ferocity"])

table.add_row(["wolverine", 100])
table.add_row(["grizzly", 87])
table.add_row(["cat", -1])
table.add_row(["dolphin", 63])

print(table)
