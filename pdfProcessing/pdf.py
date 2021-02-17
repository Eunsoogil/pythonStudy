# pip3 install PyPDF2
import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_test():
    with open('dummy.pdf', 'rb') as file:  # rb : read binary
        reader = PyPDF2.PdfFileReader(file)
        print(reader.numPages)
        print(reader.getPage(0))
        page = reader.getPage(0)
        page.rotateCounterClockwise(90)
        writer = PyPDF2.PdfFileWriter()  # writer 객체에 담음
        writer.addPage(page)
        with open('tilt.pdf', 'wb') as new_file:
            writer.write(new_file)


# python pdf.py dummy.pdf twopage.pdf tilt.pdf
def pdf_combine(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('merge.pdf')


# pdf_combine(inputs)
def pdf_combine_wtr():
    template = PyPDF2.PdfFileReader(open('merge.pdf', 'rb'))
    watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
    output = PyPDF2.PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open('watermarked_output.pdf', 'wb') as file:
            output.write(file)


pdf_combine_wtr()

