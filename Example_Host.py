from abstractdata import AbstractData

class Host(AbstractData):
    
    def __init__(self):
        super().__init__("host",
            [
                "node",
                "server"
            ],
            "id",
            False
            )
    
    def save(self) -> bool:
        if not self.validateNode():
            return False
        if not self.validateServer():
            return False
        if not super().save():
            return False
        return True
    
    def validateNode(self) -> bool:
        if self.__data["node"] == None:
            self.__fail = Exception("node não pode ser vazio.")
            return False

        if 'int' not in str(type(self.__data["node"])):
            self.__fail = Exception("node deve ser tipo inteiro.")
            return False

        if len(self.__data["node"]) > 5 or len(self.__data["node"]) < 4:
            self.__fail = Exception("node deve ter entre 4 a 5 caracteres.")
            return False

        return True

    def validateServer(self) -> bool:
        if self.__data["server"] == None:
            self.__fail = Exception("server não pode ser vazio.")
            return False

        if 'str' not in str(type(self.__data["server"])):
            self.__fail = Exception("server deve ser tipo texto.")
            return False

        return True

    def list(self):
        return self.find(columns="Node, NodeHost").fetch(True)

    def edit(self,node:int,host:str = None) -> bool:
        row = self.find(f"Node = %(node)s",{"node":node}).fetch()
        if row == None:
            return False
        self.__data = self.merge(row,{"NodeHost":host})
        return self.save()

host = Host()
list = host.list()
# edit = host.edit(1168,"SPNETUR68")

print(list)
# print(edit)
print(host.getData())
print(host.getFail())
    