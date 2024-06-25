import pikepdf

old_pdf = pikepdf.Pdf.open("python cheatsheet.pdf") #Here you give your pdf file which you want to protect

no_extract = pikepdf.Permissions(extract=False) #Here this line of code represent us that  users will not be able to copy text or images from the PDF.


old_pdf.save("Protected_pdf.pdf",
             encryption=pikepdf.Encryption(user="123Rashmi",# this is the password
                                           allow=no_extract)
             )