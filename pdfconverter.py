import pdfkit

options = { 
      'margin-bottom': '0.75in', 
      'footer-right': '[page] of [topage]',
     }

pdfkit.from_file('/home/bharat/Downloads/map/village_data_4.html', 'out.pdf', options=options)