from src.model.Usuario import Usuario
from src.repositories.UsuarioRepository import add_usuario

def verificar_email_caracteres_proibidos(texto):
    caracteres_proibidos = ['!', '?', '&', '*', '#', '$']
    
    for caractere in caracteres_proibidos:
        if caractere in texto:
            raise ValueError(f'A string não deve conter caracteres especiais como !,?, &, *, #, $')

def addUsuario(id: int, nome: str, email: str, senha:str) -> Usuario:
    if(id is None or id == '' or nome is None or nome == '' or nome.lower == 'puto'or nome.lower =='filha da puta' or nome.lower =='caralho'or nome.lower =='desgraça' or nome.lower == 'desgraçado' or nome.lower =='thomas turbando' or nome.lower =='sugiro ki memami' ):
        raise TypeError("E esse nome aí figura?")
    
    if any(not char.isalnum() for char in senha):
        raise ValueError("A string não deve conter caracteres especiais.")
    
    if not (any(c.isalpha() for c in senha) and any(c.isdigit() for c in senha)):
        raise TypeError("A string deve Conter numeros e letras")
    
    verificar_email_caracteres_proibidos(email)

    return add_usuario(id, nome, email, senha)