import sys

from rich.console import Console

console = Console(record=True)
file = open(sys.argv[1])
filecontent = file.read()
console.print(filecontent)
console.save_svg(sys.argv[2], title=sys.argv[1])
