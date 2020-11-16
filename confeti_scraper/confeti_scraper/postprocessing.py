import os
import re
import json


def postprocessing(filename):
    scraper_output = None
    valid_output = {}
    reports_list = []
    print(filename)
    with open(f'spiders/output/{filename}', 'r') as conf_outp:
        scraper_output = json.load(conf_outp)

    valid_output['conference'] ={
                                 'year': str(*re.findall(r'\d\d\d\d',scraper_output[0]['year'])),
                                 'name': scraper_output[0]['name'],
                                 'location': scraper_output[0]['location'],
                                 'logo': scraper_output[0]['logo'],
                                 'url': scraper_output[0]['url']
                                 }

    for output_json in scraper_output:
        reports_list.append(output_json['report'])
        
    valid_output['reports'] = reports_list

    with open(f'spiders/output/valid_outputs/{filename}','w') as v_out:
        json.dump(valid_output,v_out)


for outp_file in os.listdir('spiders/output'):
    try:
        if 'json' in outp_file:
            postprocessing(outp_file)
        else:
            continue
    except Exception as E:
        print(f'raised {E}')
