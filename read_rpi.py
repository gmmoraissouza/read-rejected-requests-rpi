import xml.etree.ElementTree as ET
import pandas as pd

def parse_xml_to_excel(xml_file, output_file):
    
    tree = ET.parse(xml_file)
    root = tree.getroot()

    process_data = []

    for process in root.findall('processo'):
        number = process.get('numero')
        
        dispatch = process.find("despachos/despacho")
        dispatch_code = dispatch.get("codigo") if dispatch is not None else None
        dispatch_name = dispatch.get("nome") if dispatch is not None else None

        dismissed = dispatch_name == "Indeferimento do pedido"

        if dismissed:

            holders = process.find("titulares/titular")
            holders_name = holders.get("nome-razao-social") if holders is not None else None
            holders_country = holders.get("pais") if holders is not None else None
            holders_state = holders.get("uf") if holders is not None else None

            class_nice = process.find("lista-classe-nice/classe-nice")
            class_code = class_nice.get("codigo") if class_nice is not None else None
            class_specification = class_nice.find("especificacao").text if class_nice is not None else None
            class_status = class_nice.find("status").text if class_nice is not None else None

            process_data.append({
                "Numero do Processo": number,
                "Despacho Codigo": dispatch_code,
                "Despacho Nome": dispatch_name,
                "Texto Complementar": dispatch.find("texto-complementar").text if dispatch is not None else None,
                "Titular Nome": holders_name,
                "Titular Pais": holders_country,
                "Titular UF": holders_state,
                "Classe Codigo": class_code,
                "Classe Especificacao": class_specification,
                "Classe Status": class_status
            })

    df = pd.DataFrame(process_data)

    df.to_excel(output_file, index=False)
    print(f"Arquivo salvo em {output_file}")

xml_file = "rpi_archive.xml"
output_file = "result.xlsx"

parse_xml_to_excel(xml_file, output_file)
