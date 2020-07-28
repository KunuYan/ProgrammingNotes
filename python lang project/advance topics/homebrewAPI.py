import requests, json

r = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = r.json()

#packages_str = json.dumps(packages_json, indent=2)
#print(packages_str)


#make an analytics json
def make_analytic(packages_json):
    analytics_json = {}
    len_pkgs_json = len(packages_json)
    counter = 0
    for package in packages_json:
        package_name = package['name']
        package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'
        res = requests.get(package_url)
        package_json = res.json()
        installs_30 = package_json['analytics']['install_on_request']['30d'][package_name]
        installs_90 = package_json['analytics']['install_on_request']['90d'][package_name]
        installs_365 = package_json['analytics']['install_on_request']['365d'][package_name]
        analytics_json[package_name]= {
            'installs_30':installs_30,
            'installs_90':installs_90,
            'installs_365':installs_365
            }
        counter += 1
        len_pkgs_json = counter*100/len_pkgs_json
        print(f'Loading: {counter}/{len_pkgs_json}, {len_pkgs_json}%')

    #analytics_str = json.dumps(analytics_json, indent=2)
    return analytics_json

analytics_json = make_analytic(packages_json)
aalib_analytics = analytics_json['aalib']
print(aalib_analytics)