from django.http import HttpResponse
import csv
from io import StringIO
from odf.opendocument import OpenDocumentSpreadsheet
from odf.style import Style, TextProperties, TableColumnProperties
from odf.text import P
from odf.table import Table, TableRow, TableCell

mimetypes = {"csv": "text/csv", \
        "ods": "application/vnd.oasis.opendocument.spreadsheet"}

def export_csv (headers, data):
    buffer = StringIO ()
    writer = csv.writer (buffer)
    if len (headers) > 0:
        writer.writerow (headers)
    for line in data:
        writer.writerow (line)

    return buffer.getvalue ()

def txt(msg):
    text = msg
    if not isinstance(msg, unicode):
        text = unicode (msg, "utf-8")
    return text

def export_ods (headers, data):
    doc = OpenDocumentSpreadsheet()
    style = Style(name="Large number", family="table-cell")
    style.addElement(TextProperties(fontfamily="Arial", fontsize="15pt"))
    doc.styles.addElement(style)
    widewidth = Style(name="co1", family="table-column")
    widewidth.addElement(TableColumnProperties(columnwidth="2.8cm", breakbefore="auto"))
    doc.automaticstyles.addElement(widewidth)

    table = Table()
    if len (headers) > 0:
        tr = TableRow ()
        table.addElement (tr)
        for item in headers:
            tc = TableCell ()
            tr.addElement (tc)
            p = P(stylename = style, text = txt(item))
            tc.addElement (p)

    for line in data:
        tr = TableRow ()
        table.addElement (tr)
        for item in line:
            tc = TableCell ()
            tr.addElement (tc)
            p = P (stylename = style, text = txt(item))
            tc.addElement (p)

    doc.spreadsheet.addElement(table)
    buffer = StringIO ()
    doc.write(buffer)

    return buffer.getvalue ()


def exportateur (headers = [], data = [], type = "csv", filename = None):
    content = None
    if type == "csv":
        content = export_csv (headers, data)
    elif type == "ods":
        content = export_ods (headers, data)
    else:
        raise "Type d'exportateur inconnu: %s" % type

    if filename is None:
        filename = "exportateur.%s" % type

    response = HttpResponse (mimetype = mimetypes[type])
    response['Content-Disposition'] = "attachment; filename=\"%s\"" % filename
    response.write (content)

    return response
