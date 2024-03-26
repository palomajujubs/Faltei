from passlib.context import CryptContext
#constante que cria hash 
CRIPTO = CryptContext(schemes=['bcrypt'], deprecated= 'auto')


def verificar_senha(senha: str , hash_senha: str)-> bool:
    #fução que verifica se senha informada é igual a senha hash
    return CRIPTO.verify(senha, hash_senha)


def gerar_hash_senha(senha: str)->str:
    return CRIPTO.hash(senha)
