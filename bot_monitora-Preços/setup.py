import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluído na pasta final

# Saida de arquivos
configuracao = Executable(
    script='pesquisa.py',
    icon='icon.ico'
)
# Configurar o executável
setup(
    name='Pesquisador de Preço do Iphone 15 max pro',
    version='1.0',
    description='Este programa automatiza pesquisa de preço emum site específico',
    author='Cleber W. Sena',
    options={'build_exe':{        
        'include_msvcr': True
    }},
    executables=[configuracao]
)