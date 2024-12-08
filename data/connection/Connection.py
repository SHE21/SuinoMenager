from peewee import MySQLDatabase
from peewee import OperationalError

class Connection:
    def __init__(self):
        self.db_name = "suino"
        self.user = "root"
        self.password = "shekespeare21"
        self.host = "localhost"
        self.port = 3306
        self.db = None

    def connect(self):
        """Cria a conexão com o banco de dados MySQL."""
        try:
            self.db = MySQLDatabase(self.db_name, user=self.user, password=self.password, host=self.host, port=self.port)
            self.db.connect()
            print("✅ Conexão com o banco de dados estabelecida com sucesso!")
        except OperationalError as e:
            print(f"❌ Erro ao conectar ao banco de dados: {e}")

    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.db and not self.db.is_closed():
            self.db.close()
            print("🔌 Conexão com o banco de dados fechada.")

    def get_db(self):
        """Retorna o objeto do banco de dados."""
        return self.db

if __name__ == "__main__":
    Connection().connect()