import requests #Husk å kjøre pip install requests i terminalen først:)

#Liste med alle eksamensoppgaver og LF
pdf_links = ['https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/E_TFY4107_231204.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/L_TFY4107_231204.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/E_TFY4107_230808.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/L_TFY4107_230808.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/E_TFY4107_221214.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/L_TFY4107_221214.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/E_TFY4107_220816.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/L_TFY4107_220816.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/E_TFY4107_211215.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/L_TFY4107_211215.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/E_TFY4107_201216.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/L_TFY4107_201216.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/E_TFY4107_200603.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/L_TFY4107_200603.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/E_TFY4109_191216.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/L_TFY4109_191216.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/E_TFY4109_181206.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/L_TFY4109_181206.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/E_TFY4109_171216.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/L_TFY4109_171216.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/E_TFY4109_160809.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/L_TFY4109_160809.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/E_TFY4109_151214.pdf', 'https://stovneng.folk.ntnu.no/EKSAMENSARKIV/TFY4107/L_TFY4109_151214.pdf']



def download_pdfs(links):
    for i, link in enumerate(links, start=1):
        link_version=link[52:53]
        if link_version=="L":
            link_version+="F_"
        else:
            link_version+="KS_"
        
        link_date=link[62:66]
        link_year=link_date[0:2]
        
        link_month=link_date[2:4]
        if int(link_month)>10:
            link_month="H"
        else:
            link_month="K"
        
        response = requests.get(link)
        if response.status_code == 200:  
            filename = f"{link_version+link_month+link_year}.pdf"
            
            with open(filename, "wb") as file:
                file.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download: {link} (Status code: {response.status_code})")
download_pdfs(pdf_links)
