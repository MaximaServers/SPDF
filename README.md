# SPDF
###### Versión 1.0 - Beta - En estado de pruebas

Lectura, Extracción, Unión y Creación de PDF basado en librerias ya existentes de Python

Basado en las librerias:

  - PyPDF2
  - xhtml2pdf
  - pdftotext
  
Usado para aplicaciones Flask.

## Examples

### Extract text from PDF:

```
>>> from spdf import Extract
>>> _ = Extract('/path/to/valid/pdf.pdf')
>>> _
>>> <spdf.Extract object at 0x1025f59e8>
>>> _.echo_pdf()
>>> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ut porta massa. Donec in metus eu elit dictum mollis vel ut massa. Mauris bibendum sollicitudin leo, in rutrum nulla accumsan non. Suspendisse porttitor feugiat ante eu venenatis. Nulla sollicitudin congue lorem, vel facilisis odio eleifend eu. Sed ac cursus quam, quis aliquam sapien. Fusce interdum risus nec arcu dignissim, ac venenatis est congue. Proin egestas posuere ex, id aliquam arcu condimentum vitae. Fusce semper laoreet nibh quis hendrerit. Suspendisse mollis quis risus in fringilla. In ac neque eu nulla varius porta. Nunc luctus elit vel nisi lacinia porttitor. In imperdiet enim eget commodo consectetur. Ut eu odio tortor. Nunc aliquet felis iaculis dolor malesuada tempus a aliquam purus. Etiam porta odio vel urna posuere, non viverra velit viverra.
```

### Create PDF from PNG or JPEG image:
```
>>> from spdf import SPDF
>>> _ = SPDF()
>>> _
>>> <spdf.SPDF object at 0x1016d9b38>
>>> _.img_to_pdf('/path/to/valid/image.jpg')
>>> <PyPDF2.pdf.PdfFileReader object at 0x108792cf8>
```

### Merge PDF to other PDF
```
>>> from spdf import Merge
>>> _ = Merge()
>>> _
>>> <spdf.Merge object at 0x1028b74a8>
>>> _.prepare_one('path/to/valid/pdf.pdf')
>>> _.to_merge_to('newfile.pdf')
>>> "newfile.pdf"
```

### Excepciones
En el momento que haya alguna falla derivada de los procedimientos en SPDF, se lanza SPDF_R como atrapador de excepciones.

### Documentación completa en:
##### http://spdf.mipropia.com/
