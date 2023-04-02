from collections import namedtuple 
Fish =namedtuple("Fish", ['nombre','especie','tanque'])
# Crea clase Fish con atributos publicos 
miprimerpez= Fish('Andres','PT','Tanque grande')

print(miprimerpez)

print(miprimerpez._asdict())