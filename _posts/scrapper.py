import os
import glob

# obtener los filepaths
casas_md = sorted(glob.glob('*.md'), key=os.path.getmtime)

# header_area
header = 'var tipueslide = {\"pages\": [{\"title\":\"MARAZUL\", \"text\": \"Nosotros nosotros Ofertas ofertas Destacados destacados Venta venta Renta renta\", \"img\": \"/img/portada.jpg\", \"url\": \"index.html\"},{\"title\":\"Contacto\", \"text\": \"Contacto contacto. Suscríbete suscribete Ofertas ofertas especiales. Hilario Malpica No. 33, Fracc. Costa Azul, Acapulco Gro. Tel tel (744) 104 0619 Información información ? Correo correo male.muce@gmail.com\", \"note\":\"Ponte en contacto con nosotros\", \"img\": \"/img/contact.jpeg\", \"url\": \"index.html#contacto\"},{\"title\": \"@marazul\", \"text\": \"facebook Facebook\", \"url\": \"https://www.facebook.com/casasmarazul/\"},'
# footer_area
footer = '{\"title\": \"@marazul\", \"text\": \"twitter Twitter\", \"url\": \"https://www.facebook.com/casasmarazul/\"}]};'
# body_area
body = ''

# crear los tags
for casa in casas_md:
    title = ""
    url= "https://malenamuce.github.io/" + casa.replace('-','/').replace('.md','.html')
    tag = ""
    img_url = ""
    with open(casa) as file:
        for i, line in enumerate(file):
            if i == 3:
                title = line.strip('title: ').strip('\n')
            elif i in [5,8,9,13,14,15,16]:
                tag = tag + line.replace('\n',' ').strip('"')
            elif i == 23:
                img_url = line.strip('  - ').strip('\n')
                break
    body = body + '{\"title\": \"' + title + '\", \"text\": \"' + tag + '\", \"img\": \"' + img_url + '\", \"url\": \"' + url + '\"},'

file = open("../js/tipueslide/tipueslide_content.js", "w")
file.write(header + body + footer)
file.close()
