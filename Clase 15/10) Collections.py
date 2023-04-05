from collections import namedtuple 
D =namedtuple("Fish", ['nombre','especie','tanque'])
# Crea clase Fish con atributos publicos 
miprimerpez= D('Andres','PT','Tanque grande')

print(miprimerpez)

print(miprimerpez._asdict())