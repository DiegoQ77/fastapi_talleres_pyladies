from app.repositories.unit_of_work import UnitOfWork


class ProductService:
    def __init__(self, unit_of_work=UnitOfWork()) -> None:
        self.__unit_of_work = unit_of_work
    
    def get_products(self) -> None:
        try:
            programs_list = self.__unit_of_work.products.list()
            print("soy unit of work")
            print(programs_list[0].name)
            print(self.__unit_of_work)
            return None
        except Exception as e:
            raise   
    