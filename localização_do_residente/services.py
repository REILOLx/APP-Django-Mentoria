from .models import Endereco,Residente

class EnderecoServices:


    @staticmethod
    def get(id_endereco):
        try:
            endereco = Endereco.objects.get(id_endereco=id_endereco)
            return endereco
        except:
            return None
        
    @staticmethod
    def query_all():
        endereco = Endereco.objects.all()
        return endereco
    
class ResidenteServices:


    @staticmethod
    def get(id_residente):
        try:
            residente = Residente.objects.get(id_residente=id_residente)
            return residente
        except:
            return None
        
    @staticmethod
    def query_all():
        residente = Residente.objects.all()
        return residente