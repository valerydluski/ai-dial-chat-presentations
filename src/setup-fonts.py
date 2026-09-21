"""Link locally licensed system fonts for the portable macOS renderer."""
from pathlib import Path
root=Path(__file__).resolve().parent.parent
out=root/'tools/LibreOffice.app/Contents/Resources/fonts/truetype'
if not out.exists():raise SystemExit('Portable macOS LibreOffice not found; configure fonts in your system renderer.')
for name in ['Arial','Arial Bold','Arial Italic','Arial Bold Italic','Courier New','Courier New Bold','Courier New Italic','Courier New Bold Italic']:
 source=Path('/System/Library/Fonts/Supplemental')/(name+'.ttf');target=out/source.name
 if not source.exists():raise SystemExit('Missing installed font: '+str(source))
 if not target.exists():target.symlink_to(source)
print('Local Arial and Courier New font links are ready.')
