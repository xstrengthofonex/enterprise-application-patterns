from patterns.table_data_gateway.gateways.person_gateway import PersonGateway
from patterns.table_data_gateway.migrations.create_person_table import upgrade

if __name__ == "__main__":
    upgrade()

    whites = PersonGateway.find_with_lastname("White")
    for row in whites:
        print("{} {} has {} dependents".format(row['firstname'],
            row['lastname'], row['numberOfDependents']))
    print()

    yeomans = PersonGateway.find_with_lastname("Yeoman")
    for row in yeomans:
        print("{} {} has {} dependents".format(row['firstname'],
            row['lastname'], row['numberOfDependents']))