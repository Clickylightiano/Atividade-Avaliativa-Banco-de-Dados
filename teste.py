import sqlite3
from pathlib import Path
ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "teste_banco.sqlite")
cursor = conexao.cursor()