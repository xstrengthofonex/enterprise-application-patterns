from table_data_gateway.person_gateway import PersonGateway

if __name__ == "__main__":
    people = PersonGateway.find_all()
    print(people)

    whites = PersonGateway.find_with_lastname("White")
    print(whites)