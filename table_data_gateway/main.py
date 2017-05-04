from table_data_gateway.person_gateway import PersonGateway

if __name__ == "__main__":
    whites = PersonGateway.find_with_lastname("White")
    for row in whites:
        print("{} {} has {} dependents".format(row['firstname'],
            row['lastname'], row['numberOfDependents']))

    print()
    yeomans = PersonGateway.find_with_lastname("Yeoman")
    for row in yeomans:
        print("{} {} has {} dependents".format(row['firstname'],
            row['lastname'], row['numberOfDependents']))