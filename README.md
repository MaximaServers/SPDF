# SPDF
Lectura, Extracción, Unión y Creación de PDF basado en librerias ya existentes de Python

Basado en las librerias:

  - PyPDF2
  - xhtml2pdf
  - pdftotext
  
Commonly used for Flask Apps.

## Examples

### Extract text from PDF:

```python
>>> from spdf import Extract
>>> _ = Extract('/path/to/valid/pdf.pdf')
>>> _
>>> <spdf.Extract object at 0x1025f59e8>
>>> _.echo_pdf()
>>> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ut porta massa. Donec in metus eu elit dictum mollis vel ut massa. Mauris bibendum sollicitudin leo, in rutrum nulla accumsan non. Suspendisse porttitor feugiat ante eu venenatis. Nulla sollicitudin congue lorem, vel facilisis odio eleifend eu. Sed ac cursus quam, quis aliquam sapien. Fusce interdum risus nec arcu dignissim, ac venenatis est congue. Proin egestas posuere ex, id aliquam arcu condimentum vitae. Fusce semper laoreet nibh quis hendrerit. Suspendisse mollis quis risus in fringilla. In ac neque eu nulla varius porta. Nunc luctus elit vel nisi lacinia porttitor. In imperdiet enim eget commodo consectetur. Ut eu odio tortor. Nunc aliquet felis iaculis dolor malesuada tempus a aliquam purus. Etiam porta odio vel urna posuere, non viverra velit viverra.
```

### Create PDF from PNG or JPEG image:
```python
>>> from spdf import SPDF
>>> _ = SPDF()
>>> _
>>> <spdf.SPDF object at 0x1016d9b38>
>>> _.img_to_pdf('/path/to/valid/image.jpg')
>>> <PyPDF2.pdf.PdfFileReader object at 0x108792cf8>
```
