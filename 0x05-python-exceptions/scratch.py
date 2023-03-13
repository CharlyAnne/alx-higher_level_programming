class User:
    id = 89
    name = "no name"
 = None
    
    def__init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

u = User()
u.name